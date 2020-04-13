"""
Module contains  posts
"""

from api.models.core import Post
from api.songs.serializers import SongSerializer
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for posts
    """

    song = SongSerializer(read_only=True)

    class Meta:
        """
        Serializer Meta Definition
        """

        model = Post
        fields = "__all__"
