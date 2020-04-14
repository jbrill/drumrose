"""
Album Serializer
"""

from api.models.core import Album
from rest_framework import serializers


class AlbumSerializer(serializers.ModelSerializer):
    """
    Serializer for Album
    """

    artwork_url = "HELLO"

    class Meta:
        """
        Serializer Meta Definition
        """

        model = Album
        fields = "__all__"
