"""
 User Route Module
"""

import json

from api.models.core import UserProfile
from api.users.serializers import UserSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


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

    def get(self, request):
        """
        Description:
            Fetches all users
        Routes:
            Retrieves a list of all users
        """
        users = UserProfile.objects.all()
        serializer = UserSerializer(users, many=True)
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
        serializer = UserSerializer(data=data)
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

        serializer = UserSerializer(user)
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

        serializer = UserSerializer(user)
        return Response(serializer.data)

    def delete(self, request, user_handle):
        """
        DELETE for UserDetail
        """
        print(request)
        user = UserProfile.objects.get(handle=user_handle)

        user.delete()

        serializer = UserSerializer(user)
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
        serializer = UserSerializer(followers, many=True)
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
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
