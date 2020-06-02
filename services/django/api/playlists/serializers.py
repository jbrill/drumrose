"""
Module contains playlist serializers
"""

from api.models.core import Playlist
from rest_framework import serializers


class PlaylistSerializer(serializers.ModelSerializer):
    """
    Serializer for playlists
    """

    class Meta:
        """
        Serializer Meta Definition
        """

        model = Playlist
        fields = "__all__"
