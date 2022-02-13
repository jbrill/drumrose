from api.models.core import (
    UserProfile,
    TrackReview,
    AlbumReview,
    PlaylistReview,
    FavoritedTrack,
)
from rest_framework import serializers


class UserProfileSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length=200)
    auth0_user_id = serializers.CharField(max_length=200)
    following = serializers.SerializerMethodField("get_following_list")
    followers = serializers.SerializerMethodField("get_followers_list")
    track_reviews = serializers.SerializerMethodField("get_track_reviews_list")
    album_reviews = serializers.SerializerMethodField("get_album_reviews_list")
    playlist_reviews = serializers.SerializerMethodField("get_playlist_reviews_list")
    favorite_tracks = serializers.SerializerMethodField("get_favorited_tracks_list")

    class Meta:
        model = UserProfile
        fields = "__all__"

    def get_following_list(self, obj):
        return [follow.following_user.id for follow in obj.following.all()]

    def get_followers_list(self, obj):
        return [follow.follower_user.id for follow in obj.followers.all()]

    def get_track_reviews_list(self, obj):
        return [review.review for review in TrackReview.objects.filter(user=obj)]

    def get_album_reviews_list(self, obj):
        return [review.review for review in TrackReview.objects.filter(user=obj)]

    def get_playlist_reviews_list(self, obj):
        return [review.review for review in TrackReview.objects.filter(user=obj)]

    def get_favorited_tracks_list(self, obj):
        return [track.id for track in FavoritedTrack.objects.filter(user=obj)]

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
