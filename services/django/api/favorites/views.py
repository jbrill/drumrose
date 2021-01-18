"""
Favorites Route Definitions
"""
# pylint: disable=W0612,W0613
from itertools import chain
from operator import attrgetter

from api.favorites.serializers import (
    FavoritedAlbumSerializer,
    FavoritedPlaylistSerializer,
    FavoritedSerializer,
    FavoritedTrackSerializer,
)
from api.models.core import (
    FavoritedAlbum,
    FavoritedPlaylist,
    FavoritedTrack,
    UserProfile,
    Song,
    Playlist,
    Album,
)
from django.core.paginator import Paginator
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
        GET /favorites/tracks/
            Gets a list of favorited tracks
    """

    authentication_classes = [Auth0JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Get favorited tracks
        """
        favorites = FavoritedTrack.objects.all()

        return JsonResponse(
            {"favorited_tracks": list(favorites.values())}, status=status.HTTP_200_OK
        )

    def post(self, request):
        """
        Create favorited track
        """
        user = UserProfile.objects.get(
            auth0_user_id=str(request.user).replace(".", "|")
        )
        song = Song.objects.get(apple_music_id=request.data["apple_music_id"])
        try:
            serializer = FavoritedTrackSerializer(
                data={
                    "apple_music_id": song.apple_music_id,
                    "auth0_user_id": user.auth0_user_id,
                }
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
        favorites = FavoritedAlbum.objects.all()

        return JsonResponse(
            {"favorited_albums": list(favorites.values())}, status=status.HTTP_200_OK
        )

    def post(self, request):
        """
        Create favorited album
        """
        try:
            user = UserProfile.objects.get(
                auth0_user_id=str(request.user).replace(".", "|")
            )
            album = Album.objects.get(apple_music_id=request.data["apple_music_id"])
            serializer = FavoritedAlbumSerializer(
                data={
                    "apple_music_id": album.apple_music_id,
                    "auth0_user_id": user.auth0_user_id,
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
        favorites = FavoritedPlaylist.objects.all()

        return JsonResponse(
            {"favorited_playlists": list(favorites.values())}, status=status.HTTP_200_OK
        )

    def post(self, request):
        """
        Post favorited playlist
        """
        try:
            user = UserProfile.objects.get(
                auth0_user_id=str(request.user).replace(".", "|")
            )
            playlist = Playlist.objects.get(
                apple_music_id=request.data["apple_music_id"]
            )
            serializer = FavoritedPlaylistSerializer(
                data={
                    "apple_music_id": playlist.apple_music_id,
                    "auth0_user_id": user.auth0_user_id,
                }
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
