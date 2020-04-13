"""
Album serializer
"""

from api.models.core import Album
from rest_framework import serializers


class AlbumSerializer(serializers.Serializer):
    """
    Serializer for Album
    """

    model = Album
    fields = "__all__"
