"""
 User Route Module
"""

import json

from api.models.core import User
from api.users.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


class UserList(APIView):
    """
    Description:
        - API View for User List
    Routes:
        - GET /users/
            - Retrieves a list of all users
        - POST /users/
            - Creates a new user
    """

    def get(self, request):
        """
        Get for UserList
        """
        print(request)
        users = User.objects.all()
        print("USERS")
        print(users.count())
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Post for UserList
        """
        # create new user
        request_body = json.loads(request.body.decode("utf-8"))

        new_user = User.objects.create(
            name=request_body["name"],
            handle=request_body["handle"],
            avatar_url=request_body["avatar_url"],
        )

        serializer = UserSerializer(new_user)
        return Response(serializer.data)


class UserDetail(APIView):
    """
    Description:
        - API View for User Detail
    Routes:
        - GET /users/:user_handle
            - Gets a user
        - PATCH /users/:user_handle
            - Updates a user
        - DELETE /users/:user_handle
            - Deletes a user
    """

    def get(self, user_handle):
        """
        GET for UserDetail
        """
        user = User.objects.get(handle=user_handle)

        serializer = UserSerializer(user)
        return Response(serializer.data)

    def patch(self, request, user_handle):
        """
        PATCH for UserDetail
        """
        user = User.objects.get(handle=user_handle)

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
        user = User.objects.get(handle=user_handle)

        user.delete()

        serializer = UserSerializer(user)
        return Response(serializer.data)
