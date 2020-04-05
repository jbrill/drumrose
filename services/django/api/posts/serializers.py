"""
Module contains  posts
"""

from rest_framework import serializers
from api.models.core import Post
from api.songs.serializers import SongSerializer
from api.users.serializers import UserSerializer


class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for posts
    """
    song = SongSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        """
        Serializer Meta Definition
        """
        model = Post
        fields = ('song', 'caption', 'user')
