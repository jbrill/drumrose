from api.albums.serializers import AlbumSerializer
from api.artists.serializers import ArtistSerializer
from api.models.core import Song
from rest_framework import serializers


class SongSerializer(serializers.ModelSerializer):
    artists = ArtistSerializer(many=True, read_only=True)
    albums = AlbumSerializer(many=True, read_only=True)

    class Meta:
        model = Song
        fields = "__all__"
