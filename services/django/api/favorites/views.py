"""
Favorites Route Definitions
"""
# pylint: disable=W0612,W0613
import json
from itertools import chain
from operator import attrgetter

from api.favorites.serializers import (
    FavoritedAlbumSerializer,
    FavoritedPlaylistSerializer,
    FavoritedSerializer,
    FavoritedTrackSerializer,
)
from api.models.core import (
    Album,
    Artist,
    FavoritedAlbum,
    FavoritedPlaylist,
    FavoritedTrack,
    Song,
    UserProfile,
)
from api.users.serializers import UserProfileSerializer
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_auth0.authentication import Auth0JSONWebTokenAuthentication


class FavoriteTracksList(APIView):
    """
    Description:
        API View for Favorited Tracks
    Routes:
        GET /favorites/
            Gets a list of favorited tracks
    """

    authentication_classes = [Auth0JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Get favorited tracks
        """
        favorited_tracks = FavoritedTrack.objects.all()

        serializer = FavoritedTrackSerializer(favorited_tracks, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        """
        Create favorited track
        """
        try:
            serializer = FavoritedTrackSerializer(
                data={
                    "apple_music_id": request.data["apple_music_id"],
                    "name": request.data["name"],
                },
                context={"request": request},
            )
        except KeyError:
            return JsonResponse(
                {"message": "Missing data required for serialization."},
                status=status.HTTP_422_UNPROCESSABLE_ENTITY,
            )
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(
                serializer.data, status=status.HTTP_201_CREATED, safe=False
            )
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FavoriteAlbumList(APIView):
    """
    Description:
        API View for Favorited Albums
    Routes:
        GET /favorites/albums/
            Gets a list of favorited albums
        POST /favorites/albums/
            Creates a new favorited album
    """

    authentication_classes = [Auth0JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Get favorited albums
        """
        favorited_albums = FavoritedAlbum.objects.all()

        serializer = FavoritedAlbumSerializer(favorited_albums, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        """
        Create favorited album
        """
        try:
            serializer = FavoritedAlbumSerializer(
                data={
                    "apple_music_id": request.data["apple_music_id"],
                    "name": request.data["name"],
                },
                context={"request": request},
            )
        except KeyError:
            return JsonResponse(
                {"message": "Missing data required for serialization."},
                status=status.HTTP_422_UNPROCESSABLE_ENTITY,
            )
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(
                serializer.data, status=status.HTTP_201_CREATED, safe=False
            )
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FavoritePlaylistList(APIView):
    """
    Description:
        API View for Favorited Playlists
    Routes:
        - GET /favorites/playlists/
            - Gets a list of favorited playlists
        - POST /favorites/playlists/
            - Creates a new favorited playlist
    """

    authentication_classes = [Auth0JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Get favorited playlists
        """
        favorited_playlists = FavoritedPlaylist.objects.all()

        serializer = FavoritedPlaylistSerializer(favorited_playlists, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        """
        Post favorited playlist
        """

        return


class FollowersFavoritesList(APIView):
    """
    Description:
        API View for Followers' Favorites
    Routes:
        GET /favorites/
            Gets a list of followers' favorites
    """

    authentication_classes = [Auth0JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Get favorites from followers
        """
        favorited_playlists = FavoritedPlaylist.objects.all()
        favorited_tracks = FavoritedTrack.objects.all()
        favorited_albums = FavoritedAlbum.objects.all()

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


class FavoritesList(APIView):
    """
    Description:
        API View for Favorites
    Routes:
        GET /favorites/
            Gets a list of favorites
    """

    authentication_classes = [Auth0JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Get favorites
        """
        favorited_playlists = FavoritedPlaylist.objects.all()
        favorited_tracks = FavoritedTrack.objects.all()
        favorited_albums = FavoritedAlbum.objects.all()

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
