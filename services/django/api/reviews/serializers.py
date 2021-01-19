"""
Module contains serializers for favorites
"""

from api.albums.serializers import AlbumSerializer
from api.models.core import AlbumReview, PlaylistReview, TrackReview
from api.playlists.serializers import PlaylistSerializer
from api.songs.serializers import SongSerializer
from api.users.serializers import UserProfileSerializer
from rest_framework import serializers


class AlbumReviewSerializer(serializers.ModelSerializer):
    """
    Serializer for album reviews
    """

    user = UserProfileSerializer(read_only=True)
    album = AlbumSerializer(read_only=True)

    class Meta:
        """
        Serializer Meta Definition
        """

        model = AlbumReview
        fields = "__all__"


class TrackReviewSerializer(serializers.ModelSerializer):
    """
    Serializer for track reviews
    """

    user = UserProfileSerializer(read_only=True)
    track = SongSerializer(read_only=True)

    class Meta:
        """
        Serializer Meta Definition
        """

        model = TrackReview
        fields = "__all__"


class PlaylistReviewSerializer(serializers.ModelSerializer):
    """
    Serializer for playlist reviews
    """

    user = UserProfileSerializer(read_only=True)
    playlist = PlaylistSerializer(read_only=True)

    class Meta:
        """
        Serializer Meta Definition
        """

        model = PlaylistReview
        fields = "__all__"
