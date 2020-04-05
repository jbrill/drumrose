from rest_framework import serializers
from neptuneapi.models.neptune_core import NeptuneSong


class NeptuneSongSerializer(serializers.ModelSerializer):
    class Meta:
        model = NeptuneSong
        fields = ('__all__')
