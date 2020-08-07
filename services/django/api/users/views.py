"""
 User Route Module
"""

import json

from operator import attrgetter
from itertools import chain

from django.http import JsonResponse
from rest_framework import status
from api.models.core import (
    UserProfile,
    FavoritedAlbum,
    FavoritedTrack,
    FavoritedPlaylist,
)
from rest_framework.views import APIView
from api.users.serializers import UserProfileSerializer
from django.core.paginator import Paginator
from rest_framework.response import Response
from api.favorites.serializers import FavoritedSerializer
from rest_framework.permissions import AllowAny


class UserList(APIView):
    """
    Description:
        API View for User List
    Routes:
        GET /users/
            Retrieves a list of all users
        POST /users/
            Creates a new user
    """

    permission_classes = (AllowAny,)

    def get(self, request):
        """
        Description:
            Fetches all users
        Routes:
            Retrieves a list of all users
        """
        print(request.user)
        users = UserProfile.objects.all()
        serializer = UserProfileSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Route
          POST /users/
        Description
          Create a new user
        """
        request_body = json.loads(request.body.decode("utf-8"))
        data = {}
        data["email"] = request_body["user"]["email"]
        data["username"] = request_body["user"]["username"]
        data["auth0_user_id"] = request_body["user"]["id"]
        serializer = UserProfileSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    """
    Description:
        API View for User Detail
    Routes:
        GET /users/:user_handle
            Fetches a user
        PATCH /users/:user_handle
            Updates a user
        DELETE /users/:user_handle
            Deletes a user
    """

    def get(self, request, user_handle):
        """
        GET for UserDetail
        """
        user = UserProfile.objects.get(handle=user_handle)

        serializer = UserProfileSerializer(user)
        return Response(serializer.data)

    def patch(self, request, user_handle):
        """
        PATCH for UserDetail
        """
        user = UserProfile.objects.get(handle=user_handle)

        request_body = json.loads(request.body.decode("utf-8"))

        if request_body["name"]:
            user.name = request_body["name"]
        if request_body["handle"]:
            user.handle = request_body["handle"]
        if request_body["avatar_url"]:
            user.avatar_url = request_body["avatar_url"]

        user.save()

        serializer = UserProfileSerializer(user)
        return Response(serializer.data)

    def delete(self, request, user_handle):
        """
        DELETE for UserDetail
        """
        print(request)
        user = UserProfile.objects.get(handle=user_handle)

        user.delete()

        serializer = UserProfileSerializer(user)
        return Response(serializer.data)


class FollowersList(APIView):
    """
    Description:
        API View for Followers List
    Routes:
        GET /followers/<user_id>/
            Retrieves a list of all followers by user
        POST /users/<user_id>/
            Creates a new follower for that user
    """

    def get(self, request):
        """
        Description:
            Fetches all users
        Routes:
            Retrieves a list of all users
        """
        followers = UserProfile.objects.filter(
            user=UserProfile.objects.get(auth0_user_id=request.user)
        )
        serializer = UserProfileSerializer(followers, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Route
          POST /users/
        Description
          Create a new user
        """
        # request_body = json.loads(request.body.decode("utf-8"))
        # user_id = request.user
        # follower_id = request_body.get("follower_id")
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserFavoritesList(APIView):
    """
    Description:
        API View for a User's Favorites
    Routes:
        GET /<user_handle>/favorites/
            Gets a list of favorites of a user
    """

    def get(self, request, user_handle):
        """
        Get favorites by user's handle
        """
        user = UserProfile.get(username=user_handle)
        favorited_playlists = FavoritedPlaylist.objects.filter(user=user)
        favorited_tracks = FavoritedTrack.objects.filter(user=user)
        favorited_albums = FavoritedAlbum.objects.filter(user=user)

        # merge favorites
        sorted_favorites = sorted(
            chain(favorited_playlists, favorited_tracks, favorited_albums),
            key=attrgetter("created_date"),
            reverse=True,
        )
        query = Paginator(sorted_favorites, 10)
        page = query.page(1)
        favorites = page.object_list
        serializer = FavoritedSerializer(favorites, many=True)
        return JsonResponse(serializer.data, safe=False)
