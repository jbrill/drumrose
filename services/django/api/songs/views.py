"""
Song Views
"""

import json

from api.models.core import FavoritedTrack, Song, UserProfile
from api.songs.serializers import SongSerializer
from api.users.serializers import UserProfileSerializer
from django.http import JsonResponse
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_auth0.authentication import Auth0JSONWebTokenAuthentication


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
        Get all tracks
        """
        print(request)
        songs = Song.objects.all()

        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Create new user
        """
        print(request)
        print(request.body.decode("utf-8"))
        request_body = json.loads(request.body.decode("utf-8"))
        print(type(request_body))
        print(request_body["name"])
        # print(request_body["handle"])
        new_song = Song.objects.create_song(
            name=request_body["name"], apple_music_id=request_body["apple_music_id"]
        )

        serializer = SongSerializer(new_song)
        return Response(serializer.data)


class SongDetail(APIView):
    """
    Description:
        - API View for Post Detail
    Routes:
        - GET /songs/:song_id/
            - Gets a post
        - PATCH /posts/:post_id
            - Updates a post
        - DELETE /posts/:post_id
            - Deletes a post
    """

    authentication_classes = []
    permission_classes = []

    def get(self, request, apple_music_id):
        try:
            song = Song.objects.get(apple_music_id=apple_music_id)
        except Song.DoesNotExist:
            return JsonResponse(
                {"message": "Song does not exist."}, status=status.HTTP_409_CONFLICT
            )

        print(song.page_id)
        is_favorited = False

        # HACK: checks if 'logged in' by checking request username
        if request.user.username:
            is_favorited = FavoritedTrack.objects.filter(
                user=request.user, song=song
            ).exists()

        serializer = SongSerializer(song, context={"is_favorited": is_favorited})

        return JsonResponse({"track": serializer.data})

    def patch(self, request, post_id):
        print(request)
        post = UserProfile.objects.get(handle=post_id)

        # TODO: Update user

        serializer = UserProfileSerializer(post)
        return Response(serializer.data)

    def delete(self, request, post_id):
        print(request)
        post = UserProfile.objects.get(handle=post_id).delete()

        serializer = UserProfileSerializer(post)
        return Response(serializer.data)
