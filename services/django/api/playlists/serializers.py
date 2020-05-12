"""
Module contains playlist serializers
"""

from api.models.core import Playlist
from api.songs.serializers import SongSerializer
from api.users.serializers import UserSerializer
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for playlists
    """

    tracks = SongSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        """
        Serializer Meta Definition
        """

        model = Playlist
        fields = "__all__"
