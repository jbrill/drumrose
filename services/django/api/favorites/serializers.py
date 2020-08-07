"""
Module contains serializers for favorites
"""

from rest_framework import serializers
from api.models.core import (
    UserProfile,
    FavoritedAlbum,
    FavoritedTrack,
    FavoritedPlaylist,
    Auth0ManagementToken,
)
from api.services.auth0 import get_user
from api.songs.serializers import SongSerializer
from api.users.serializers import UserProfileSerializer
from api.albums.serializers import AlbumSerializer
from api.playlists.serializers import PlaylistSerializer


class FavoritedTrackSerializer(serializers.ModelSerializer):
    """
    Serializer for posts
    """

    song = SongSerializer(read_only=True)
    favorite_type = serializers.SerializerMethodField()
    user = UserProfileSerializer(read_only=True)

    class Meta:
        """
        Serializer Meta Definition
        """

        model = FavoritedTrack
        fields = "__all__"

    def get_favorite_type(self, _):
        """
        Return favorite type
        """

        return "track"

    def create(self, validated_data):
        user = UserProfile.objects.create(**validated_data)
        return user


class FavoritedAlbumSerializer(serializers.ModelSerializer):
    """
    Serializer for posts
    """

    user = UserProfileSerializer(read_only=True)
    album = AlbumSerializer(read_only=True)
    favorite_type = serializers.SerializerMethodField()

    class Meta:
        """
        Serializer Meta Definition
        """

        model = FavoritedAlbum
        fields = (
            "user",
            "album",
            "favorite_type",
        )

    def get_favorite_type(self, _):
        """
        Return favorite type
        """

        return "album"


class FavoritedPlaylistSerializer(serializers.ModelSerializer):
    """
    Serializer for posts
    """

    user = UserProfileSerializer()
    playlist = PlaylistSerializer(read_only=True)
    favorite_type = serializers.SerializerMethodField()

    class Meta:
        """
        Serializer Meta Definition
        """

        model = FavoritedPlaylist
        fields = "__all__"

    def get_favorite_type(self, _):
        """
        Return favorite type
        """

        return "playlist"


class FavoritedSerializer(serializers.ModelSerializer):
    """
    Serializer for posts
    """

    @classmethod
    def get_serializer(cls, model):
        if model == FavoritedPlaylist:
            serializer = FavoritedPlaylistSerializer
        elif model == FavoritedTrack:
            serializer = FavoritedTrackSerializer
        else:
            serializer = FavoritedAlbumSerializer
        return serializer

    def to_representation(self, instance):
        serializer = self.get_serializer(instance.__class__)
        return serializer(instance, context=self.context).data

    class Meta:
        """
        Serializer Meta Definition
        """

        fields = "__all__"
