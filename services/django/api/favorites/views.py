"""
Favorites Route Definitions
"""
# pylint: disable=W0612,W0613
import json

from operator import attrgetter
from itertools import chain

from django.http import JsonResponse
from rest_framework import status
from api.models.core import (
    Song,
    Album,
    Artist,
    UserProfile,
    FavoritedAlbum,
    FavoritedTrack,
    FavoritedPlaylist,
)
from django.db.models import Q
from rest_framework.views import APIView
from api.users.serializers import UserProfileSerializer
from django.core.paginator import Paginator
from api.favorites.serializers import (
    FavoritedSerializer,
    FavoritedAlbumSerializer,
    FavoritedTrackSerializer,
    FavoritedPlaylistSerializer,
)


class FavoriteTracksList(APIView):
    """
    Description:
        API View for Favorited Tracks
    Routes:
        GET /favorites/
            Gets a list of favorited tracks
    """

    authentication_classes = []
    permission_classes = []

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
        print(request.body)
        print(request.user.username)
        print("request.user.username")
        user = UserProfile.objects.get(auth0_user_id=request.user.username)
        song, song_created = Song.objects.get_or_create(
            apple_music_id=request.data["id"]
        )
        print(vars(song))
        print(user)
        favorited_item, created = FavoritedTrack.objects.get_or_create(
            song=song, user=user
        )
        serializer = FavoritedTrackSerializer(
            data={"user": user, "song": song}
        )
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(
                serializer.data, status=status.HTTP_201_CREATED, safe=False
            )
        return JsonResponse(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


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

    authentication_classes = []
    permission_classes = []

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
        return


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

    authentication_classes = []
    permission_classes = []

    def get(self, request):
        """
        Get favorited playlists
        """
        favorited_playlists = FavoritedPlaylist.objects.all()

        serializer = FavoritedPlaylistSerializer(
            favorited_playlists, many=True
        )
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

    def post(self, request):
        """
        Post favorite
        """
        user = UserProfile.objects.get(auth0_user_id=request.user)
        if request.data["type"] == "song":
            song, song_created = Song.objects.get_or_create(
                apple_music_id=request.data["id"]
            )
            favorited_item, created = FavoritedTrack.objects.get_or_create(
                song=song, user=user
            )
        elif request.data["type"] == "playlist":
            song, song_created = Artist.objects.get_or_create(
                apple_music_id=request.data["id"]
            )
            favorited_item, created = FavoritedPlaylist.objects.get_or_create(
                song=song, user=user
            )
        elif request.data["type"] == "album":
            song, song_created = Album.objects.get_or_create(
                apple_music_id=request.data["id"]
            )
            favorited_item, created = FavoritedAlbum.objects.get_or_create(
                song=song, user=user
            )
        serializer = FavoritedSerializer(favorited_item)
        return JsonResponse(serializer.data, safe=False)
