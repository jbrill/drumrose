"""
Module contains serializers for favorites
"""

from api.albums.serializers import AlbumSerializer
from api.models.core import FavoritedAlbum, FavoritedPlaylist, FavoritedTrack
from api.playlists.serializers import PlaylistSerializer
from api.songs.serializers import SongSerializer
from api.users.serializers import UserSerializer
from rest_framework import serializers


class FavoritedTrackSerializer(serializers.ModelSerializer):
    """
    Serializer for posts
    """

    song = SongSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        """
        Serializer Meta Definition
        """

        model = FavoritedTrack
        fields = "__all__"


class FavoritedAlbumSerializer(serializers.ModelSerializer):
    """
    Serializer for posts
    """

    album = AlbumSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        """
        Serializer Meta Definition
        """

        model = FavoritedAlbum
        fields = "__all__"


class FavoritedPlaylistSerializer(serializers.ModelSerializer):
    """
    Serializer for posts
    """

    song = SongSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    playlist = PlaylistSerializer(read_only=True)

    class Meta:
        """
        Serializer Meta Definition
        """

        model = FavoritedPlaylist
        fields = "__all__"
