from rest_framework import serializers

class AlbumSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    artwork_url = serializers.CharField(max_length=200)
