from rest_framework import serializers
from neptuneapi.models.neptune_core import NeptunePost

class NeptunePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = NeptunePost
        fields = ('song', 'caption', 'user')
