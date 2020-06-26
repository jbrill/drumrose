"""
Album Serializer
"""

from api.models.core import Album
from rest_framework import serializers


class AlbumSerializer(serializers.ModelSerializer):
    """
    Serializer for Album
    """

    class Meta:
        """
        Serializer Meta Definition
        """

        model = Album
        fields = "__all__"
