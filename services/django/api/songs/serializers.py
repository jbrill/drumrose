from rest_framework import serializers
from api.models.core import Song


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('__all__')
