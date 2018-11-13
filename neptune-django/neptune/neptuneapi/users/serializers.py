from rest_framework import serializers
from neptuneapi.models.neptune_core import NeptuneUser

class NeptuneUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NeptuneUser
        fields = ('name', 'handle', 'avatar_url', 'posts')
