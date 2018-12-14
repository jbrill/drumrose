"""
Module contains neptune posts
"""

from rest_framework import serializers
from neptuneapi.models.neptune_core import NeptunePost
from neptuneapi.songs.serializers import NeptuneSongSerializer
from neptuneapi.users.serializers import NeptuneUserSerializer

class NeptunePostSerializer(serializers.ModelSerializer):
    """
    Serializer for posts
    """
    song = NeptuneSongSerializer(read_only=True)
    user = NeptuneUserSerializer(read_only=True)

    class Meta:
        model = NeptunePost
        fields = ('song', 'caption', 'user')
