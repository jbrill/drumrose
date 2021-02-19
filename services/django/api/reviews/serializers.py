"""
Module contains serializers for favorites
"""

from api.albums.serializers import AlbumSerializer
from api.models.core import UserProfile, AlbumReview, PlaylistReview, TrackReview, Album
from api.playlists.serializers import PlaylistSerializer
from api.songs.serializers import SongSerializer
from api.users.serializers import UserProfileSerializer
from rest_framework import serializers


class AlbumReviewSerializer(serializers.ModelSerializer):
    """
    Serializer for album reviews
    """

    user = UserProfileSerializer(read_only=True)
    album = AlbumSerializer(read_only=True)

    class Meta:
        """
        Serializer Meta Definition
        """

        model = AlbumReview
        fields = "__all__"

    def validate(self, data):
        """
        Check if favorited album already exists
        """
        if AlbumReview.objects.filter(
            user__auth0_user_id=data.get("auth0_user_id"),
            album__apple_music_id=data.get("apple_music_id"),
        ).count():
            raise serializers.ValidationError("Reviewed Album Already Exists")
        if not UserProfile.objects.filter(
            auth0_user_id=data.get("auth0_user_id")
        ).exists():
            raise serializers.ValidationError("User Does Not Exist")
        return data

    def to_internal_value(self, data):
        internal_value = super().to_internal_value(data)
        apple_music_id = data.get("apple_music_id")
        auth0_user_id = data.get("auth0_user_id")
        internal_value.update(
            {"apple_music_id": apple_music_id, "auth0_user_id": auth0_user_id}
        )
        return internal_value

    def create(self, validated_data):
        user = UserProfile.objects.get(
            auth0_user_id=validated_data.get("auth0_user_id")
        )
        album, _ = Album.objects.get_or_create(
            apple_music_id=validated_data.get("apple_music_id")
        )
        return AlbumReview.objects.create(user=user, album=album)


class TrackReviewSerializer(serializers.ModelSerializer):
    """
    Serializer for track reviews
    """

    user = UserProfileSerializer(read_only=True)
    track = SongSerializer(read_only=True)

    class Meta:
        """
        Serializer Meta Definition
        """

        model = TrackReview
        fields = "__all__"


class PlaylistReviewSerializer(serializers.ModelSerializer):
    """
    Serializer for playlist reviews
    """

    user = UserProfileSerializer(read_only=True)
    playlist = PlaylistSerializer(read_only=True)

    class Meta:
        """
        Serializer Meta Definition
        """

        model = PlaylistReview
        fields = "__all__"
