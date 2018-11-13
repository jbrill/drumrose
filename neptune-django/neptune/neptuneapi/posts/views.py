from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from neptuneapi.models.neptune_core import NeptuneUser
from neptuneapi.users.serializers import NeptuneUserSerializer

import json

class NeptunePostList(APIView):
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
        users = NeptuneUser.objects.all()

        serializer = NeptuneUserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        # create new user
        print(request)
        print(request.body.decode('utf-8'))
        request_body = json.loads(request.body.decode('utf-8'))
        print(type(request_body))
        print(request_body["name"])
        print(request_body["handle"])
        new_user = NeptuneUser.objects.create(
            name=request_body["name"],
            handle=request_body["handle"],
            avatar_url=request_body["avatar_url"],
        )

        serializer = NeptuneUserSerializer(new_user)
        return Response(serializer.data)

class NeptunePostDetail(APIView):
    """
    Description:
        - API View for Post Detail
    Routes:
        - GET /posts/:post_id
            - Gets a post
        - PATCH /posts/:post_id
            - Updates a post
        - DELETE /posts/:post_id
            - Deletes a post
    """
    def get(self, request, post_id):
        user = NeptuneUser.objects.get(
            handle=user_handle
        )

        serializer = NeptuneUserSerializer(user)
        return Response(serializer.data)

    def patch(self, request, post_id):
        post = NeptuneUser.objects.get(
            handle=post_id
        )

        # Update user shit

        serializer = NeptuneUserSerializer(post)
        return Response(serializer.data)

    def delete(self, request, post_id):
        post = NeptuneUser.objects.get(
            handle=post_id
        ).delete()

        serializer = NeptuneUserSerializer(post)
        return Response(serializer.data)
