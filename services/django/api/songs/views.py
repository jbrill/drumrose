"""
Song Views
"""

import json

from api.models.core import FavoritedTrack, Song, UserProfile
from api.songs.serializers import SongSerializer
from api.users.serializers import UserProfileSerializer
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_auth0.authentication import Auth0JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


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

    authentication_classes = [Auth0JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        """
        Returns a list of songs
        """
        tracks = Song.objects.all().order_by("?")

        return JsonResponse(
            {"tracks": list(tracks.values())}, status=status.HTTP_200_OK
        )

    def post(self, request):
        """
        Returns a 201 if successful
        """
        serializer = SongSerializer(data={"apple_music_id": request.data["id"]})
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(
                serializer.data, status=status.HTTP_201_CREATED, safe=False
            )
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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

    authentication_classes = [Auth0JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, track_id):
        """
        Returns a serialized track
        """
        try:
            song = Song.objects.get(apple_music_id=track_id)
        except Song.DoesNotExist:
            return JsonResponse(
                {"message": "Track does not exist."}, status=status.HTTP_409_CONFLICT
            )

        serializer = SongSerializer(song, context={"request": request})
        return JsonResponse({"track": serializer.data})

    def patch(self, request, playlist_id):
        print(playlist_id)
        return JsonResponse({})

    def delete(self, request, playlist_id):
        print(playlist_id)
        return JsonResponse({})
