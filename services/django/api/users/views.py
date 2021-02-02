"""
User Route Module
"""

import json

from api.models.core import UserProfile
from api.users.serializers import UserProfileSerializer
from django.http import JsonResponse
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_auth0.authentication import Auth0JSONWebTokenAuthentication


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

    authentication_classes = [Auth0JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        """
        Description:
            Fetches all users
        Routes:
            Retrieves a list of all users
        """
        users = UserProfile.objects.all()
        serializer = UserProfileSerializer(users, many=True)
        return JsonResponse({"users": serializer.data})

    def post(self, request):
        """
        Route
          POST /users/
        Description
          Create a new user
        """
        try:
            print(request.data)
            serializer = UserProfileSerializer(
                data={
                    "email": request.data["email"],
                    "username": request.data["username"],
                    "auth0_user_id": request.data["id"],
                }
            )
        except KeyError:
            return JsonResponse(
                {"message": "Missing data required for serialization."},
                status=status.HTTP_422_UNPROCESSABLE_ENTITY,
            )
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PopularUserList(APIView):
    """
    API View for User List
    Routes:
        GET /users/popular/
            Retrieves a list of all users
        POST /users/popular/
            Creates a new user
    """

    authentication_classes = [Auth0JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Fetches all users by popularity
        """
        users = UserProfile.objects.all()
        serializer = UserProfileSerializer(users, many=True)
        return JsonResponse({"users": serializer.data})


class UserDetail(APIView):
    """
    API View for User Detail
    Routes:
        GET /users/:user_handle
            Fetches a user
        PATCH /users/:user_handle
            Updates a user
        DELETE /users/:user_handle
            Deletes a user
    """

    authentication_classes = [Auth0JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticated]

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
        GET /users/<user_id>/followers/
            Retrieves a list of all followers by user
        POST /users/<user_id>/followers/
            Creates a new follower for that user
    """

    authentication_classes = [Auth0JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Description:
            Retrieves a list of all followers by user
        """
        followers = UserProfile.objects.filter(
            user=UserProfile.objects.get(username=request.user.username)
        ).followers
        serializer = UserProfileSerializer(followers, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Description
          Creates a new follower request.user for the user by <user_id>
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
        GET /users/<user_handle>/favorites/
            Gets a list of favorites of a user
    """

    authentication_classes = [Auth0JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, user_handle):
        """
        Get favorites by user's handle
        """
        print(user_handle)
        return Response()
