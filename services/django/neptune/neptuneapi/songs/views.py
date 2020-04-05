from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from neptuneapi.models.neptune_core import NeptuneUser, NeptuneSong
from neptuneapi.songs.serializers import NeptuneSongSerializer

import json


class NeptuneSongList(APIView):
    """
    Description:
        - API View for User List
    Routes:
        - GET /songs/
            - Gets a list of songs per user
        - POST /songs/
            - Creates a new song
    """

    def get(self, request):
        """
        If 'feed'
          # Grab followers
            # Grab most recent posts
        If 'discover'
          # Grab recommended
        """
        songs = NeptuneSong.objects.all()

        serializer = NeptuneSongSerializer(songs, many=True)
        return Response(serializer.data)

    def post(self, request):
        # create new user
        print(request)
        print(request.body.decode('utf-8'))
        request_body = json.loads(request.body.decode('utf-8'))
        print(type(request_body))
        print(request_body["name"])
        # print(request_body["handle"])
        new_song = NeptuneSong.objects.create(
            name=request_body["name"],
            apple_music_id=request_body["apple_music_id"]
        )

        serializer = NeptuneSongSerializer(new_song)
        return Response(serializer.data)


class NeptuneSongDetail(APIView):
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
        print("HERE...")
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
