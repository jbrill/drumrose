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
    User,
)
from api.users.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


class FavoriteTracksList(APIView):
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
        - GET /posts/
            - Gets a list of posts per user
        - POST /posts/
            - Creates a new post
    """

    def get(self, request):
        """
        Get favorited tracks
        """
        favorited_playlists = FavoritedPlaylist.objects.all()
        favorited_tracks = FavoritedTrack.objects.all()
        favorited_albums = FavoritedAlbum.objects.all()

        # merge favorites
        favorites = sorted(
            chain(favorited_playlists, favorited_tracks, favorited_albums),
            key=attrgetter("created_date"),
        )
        print("efore serializer")
        serializer = FavoritedSerializer(favorites, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Post favorited playlist
        """

        return
