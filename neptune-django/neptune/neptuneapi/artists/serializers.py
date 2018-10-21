from rest_framework import serializers

class ArtistSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
