from rest_framework import serializers
from api.models.core import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'handle', 'avatar_url')
