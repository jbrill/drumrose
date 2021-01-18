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

    user = UserProfileSerializer()
    album = AlbumSerializer()

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

    user = UserProfileSerializer()
    track = SongSerializer()

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

    user = UserProfileSerializer()
    playlist = PlaylistSerializer()

    class Meta:
        """
        Serializer Meta Definition
        """

        model = PlaylistReview
        fields = "__all__"
