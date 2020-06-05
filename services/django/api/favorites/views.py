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


class PostDetail(APIView):
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
        print(post_id)
        user_handle = request.body.get("user_handle")
        user = User.objects.get(handle=user_handle)

        serializer = UserSerializer(user)
        return Response(serializer.data)

    def patch(self, request, post_id):
        print(request)
        post = User.objects.get(handle=post_id)

        # Update user shit

        serializer = UserSerializer(post)
        return Response(serializer.data)

    def delete(self, request, post_id):
        print(request)
        post = User.objects.get(handle=post_id).delete()

        serializer = UserSerializer(post)
        return Response(serializer.data)


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

        serializer = FavoritedSerializer(favorites, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Post favorited playlist
        """

        return
