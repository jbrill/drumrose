from api.models.core import UserProfile
from rest_framework import serializers


class UserProfileSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length=200)
    auth0_user_id = serializers.CharField(max_length=200)

    class Meta:
        model = UserProfile
        fields = "__all__"

    def validate_email(self, value):
        """
        Validate uniqueness constraints
        """
        if UserProfile.objects.filter(email=value).count():
            raise serializers.ValidationError("A user with this email already exists.")
        return value

    def validate_username(self, value):
        """
        Validate uniqueness constraints
        """
        if UserProfile.objects.filter(username=value).count():
            raise serializers.ValidationError(
                "A user with this username already exists."
            )
        return value

    def validate_auth0_user_id(self, value):
        """
        Validate uniqueness constraints
        """
        if UserProfile.objects.filter(auth0_user_id=value).count():
            raise serializers.ValidationError(
                "A user with this auth0 user id already exists."
            )
        return value

    def create(self, validated_data):
        user = UserProfile.objects.create(**validated_data)
        return user
