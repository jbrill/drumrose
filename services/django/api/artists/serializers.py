"""
Artist Serializer Module
"""

from api.models.core import Artist
from rest_framework import serializers


class ArtistSerializer(serializers.ModelSerializer):
    """
    Artist Serializer Class
    """

    class Meta:
        """
        Serializer Meta Definition
        """

        model = Artist
        fields = "__all__"
