"""
Artist Serializer Module
"""

from rest_framework import serializers


class ArtistSerializer(serializers.Serializer):
    """
    Artist Serializer Class
    """

    name = serializers.CharField(max_length=200)
