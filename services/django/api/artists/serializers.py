"""
Artist Serializer Module
"""

from api.models.core import Artist
from rest_framework import serializers


class ArtistSerializer(serializers.Serializer):
    """
    Artist Serializer Class
    """

    model = Artist
    field = "__all__"
