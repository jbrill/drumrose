"""
Song Views
"""

import json

from api.models.core import Song, UserProfile
from api.songs.serializers import SongSerializer
from api.users.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


# from django.shortcuts import get_object_or_404
# from django.views.decorators.csrf import csrf_exempt, csrf_protect


class SongList(APIView):
    """
    Description:
        - API View for Song List
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
        print(request)
        songs = Song.objects.all()

        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data)

    def post(self, request):
        # create new user
        print(request)
        print(request.body.decode("utf-8"))
        request_body = json.loads(request.body.decode("utf-8"))
        print(type(request_body))
        print(request_body["name"])
        # print(request_body["handle"])
        new_song = Song.objects.create(
            name=request_body["name"],
            apple_music_id=request_body["apple_music_id"],
        )

        serializer = SongSerializer(new_song)
        return Response(serializer.data)


class SongDetail(APIView):
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

    def get(self, request, apple_music_id):
        track = Song.objects.get(apple_music_id=apple_music_id)

        serializer = SongSerializer(track)
        return Response(serializer.data)

    def patch(self, request, post_id):
        print(request)
        post = UserProfile.objects.get(handle=post_id)

        # TODO: Update user

        serializer = UserSerializer(post)
        return Response(serializer.data)

    def delete(self, request, post_id):
        print(request)
        post = UserProfile.objects.get(handle=post_id).delete()

        serializer = UserSerializer(post)
        return Response(serializer.data)
