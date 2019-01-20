"""
Neptune User Route Module
"""

import json

from rest_framework.views import APIView
from rest_framework.response import Response

from neptuneapi.models.neptune_core import NeptuneUser
from neptuneapi.users.serializers import NeptuneUserSerializer


class NeptuneUserList(APIView):
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
        Get for NeptuneUserList
        """
        users = NeptuneUser.objects.all()

        serializer = NeptuneUserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Post for NeptuneUserList
        """
        # create new user
        request_body = json.loads(
            request.body.decode('utf-8')
        )

        new_user = NeptuneUser.objects.create(
            name=request_body["name"],
            handle=request_body["handle"],
            avatar_url=request_body["avatar_url"],
        )

        serializer = NeptuneUserSerializer(new_user)
        return Response(serializer.data)


class NeptuneUserDetail(APIView):
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
        GET for NeptuneUserDetail
        """
        user = NeptuneUser.objects.get(
            handle=user_handle
        )

        serializer = NeptuneUserSerializer(user)
        return Response(serializer.data)

    def patch(self, request, user_handle):
        """
        PATCH for NeptuneUserDetail
        """
        user = NeptuneUser.objects.get(
            handle=user_handle
        )

        request_body = json.loads(request.body.decode('utf-8'))

        if request_body["name"]:
            user.name = request_body["name"]
        if request_body["handle"]:
            user.handle = request_body["handle"]
        if request_body["avatar_url"]:
            user.avatar_url = request_body["avatar_url"]

        user.save()

        serializer = NeptuneUserSerializer(user)
        return Response(serializer.data)

    def delete(self, request, user_handle):
        """
        DELETE for NeptuneUserDetail
        """
        user = NeptuneUser.objects.get(
            handle=user_handle
        )

        user.delete()

        serializer = NeptuneUserSerializer(user)
        return Response(serializer.data)
