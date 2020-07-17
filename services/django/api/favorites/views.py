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
    Album,
    Artist,
    FavoritedAlbum,
    FavoritedPlaylist,
    FavoritedTrack,
    Song,
)
from api.users.serializers import UserSerializer
from django.core.paginator import Paginator
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.views import APIView


class FavoriteTracksList(APIView):
    """
    Description:
        - API View for User List
    Routes:
        - GET /favorites/
            - Gets a list of posts per user
        - POST /favorites/
            - Creates a new post
    """

    authentication_classes = []
    permission_classes = []

    def get(self, request):
        """
        Get favorited tracks
        """
        favorited_tracks = FavoritedTrack.objects.all()

        serializer = FavoritedTrackSerializer(favorited_tracks, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Post favorited track
        """
        return


class FavoriteAlbumList(APIView):
    """
    Description:
        - API View for User List
    Routes:
        - GET /posts/
            - Gets a list of posts per user
        - POST /posts/
            - Creates a new post
    """

    authentication_classes = []
    permission_classes = []

    def get(self, request):
        """
        Get favorited tracks
        """
        favorited_albums = FavoritedAlbum.objects.all()

        serializer = FavoritedAlbumSerializer(favorited_albums, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Post favorited track
        """
        return


class FavoritePlaylistList(APIView):
    """
    Description:
        - API View for User List
    Routes:
        - GET /posts/
            - Gets a list of posts per user
        - POST /posts/
            - Creates a new post
    """

    authentication_classes = []
    permission_classes = []

    def get(self, request):
        """
        Get favorited tracks
        """
        favorited_playlists = FavoritedPlaylist.objects.all()

        serializer = FavoritedPlaylistSerializer(
            favorited_playlists, many=True
        )
        return Response(serializer.data)

    def post(self, request):
        """
        Post favorited playlist
        """

        return


class FavoritesList(APIView):
    """
    Description:
        - API View for User List
    Routes:
        - GET /favorites/
            - Gets a list of favorites of friends
        - POST /favorites/
            - Creates a new favorite
    """

    def get(self, request):
        """
        Get favorites
        """
        favorited_playlists = FavoritedPlaylist.objects.filter(
            ~Q(auth0_user_id=request.user.username)
        )
        favorited_tracks = FavoritedTrack.objects.filter(
            ~Q(auth0_user_id=request.user.username)
        )
        favorited_albums = FavoritedAlbum.objects.filter(
            ~Q(auth0_user_id=request.user.username)
        )

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
        return Response(serializer.data)

    def post(self, request):
        """
        Post favorite
        """
        if request.data["type"] == "track":
            song, song_created = Song.objects.get_or_create(
                apple_music_id=request.data["id"]
            )
            favorited_item, created = FavoritedTrack.objects.get_or_create(
                song=song, auth0_user_id=request.user.username
            )
        elif request.data["type"] == "playlist":
            song, song_created = Artist.objects.get_or_create(
                apple_music_id=request.data["id"]
            )
            favorited_item, created = FavoritedPlaylist.objects.get_or_create(
                song=song, auth0_user_id=request.user.username
            )
        elif request.data["type"] == "album":
            song, song_created = Album.objects.get_or_create(
                apple_music_id=request.data["id"]
            )
            favorited_item, created = FavoritedAlbum.objects.get_or_create(
                song=song, auth0_user_id=request.user.username
            )
        serializer = FavoritedSerializer(favorited_item)
        return Response(serializer.data)
