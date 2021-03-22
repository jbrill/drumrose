"""
Album Serializer
"""

from api.models.core import Album, FavoritedAlbum, AlbumReview
from rest_framework import serializers
from django.db.models import Avg


class AlbumSerializer(serializers.ModelSerializer):
    """
    Serializer for Album
    """

    favorited = serializers.SerializerMethodField(read_only=True)
    review_summary = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Album
        fields = "__all__"

    def get_review_summary(self, obj):
        album_reviews = AlbumReview.objects.filter(
            album__apple_music_id=obj.apple_music_id
        )
        review_count = album_reviews.count()
        average_review = album_reviews.aggregate(Avg("rating"))
        return {
            "total_reviews": review_count,
            "average_review": average_review.get("rating__avg"),
            "totals_per_rating": {
                "0.0": album_reviews.filter(rating=0.0).count(),
                "0.5": album_reviews.filter(rating=0.5).count(),
                "1.0": album_reviews.filter(rating=1.0).count(),
                "1.5": album_reviews.filter(rating=1.5).count(),
                "2.0": album_reviews.filter(rating=2.0).count(),
                "2.5": album_reviews.filter(rating=2.5).count(),
                "3.0": album_reviews.filter(rating=3.0).count(),
                "3.5": album_reviews.filter(rating=3.5).count(),
                "4.0": album_reviews.filter(rating=4.0).count(),
                "4.5": album_reviews.filter(rating=4.5).count(),
                "5.0": album_reviews.filter(rating=5.0).count(),
            },
        }

    def get_favorited(self, obj):
        if "request" not in self.context:
            return False
        try:
            auth0_user_id = str(self.context.get("request").user).split(".")[1]
        except IndexError:
            return False
        return FavoritedAlbum.objects.filter(
            user__auth0_user_id=auth0_user_id, album__apple_music_id=obj.apple_music_id
        ).exists()

    # pylint: disable=W0221
    def validate(self, data):
        """
        Check if favorited_track already exists
        """
        if Album.objects.filter(apple_music_id=data.get("apple_music_id")).count():
            raise serializers.ValidationError("Album Already Exists")
        return data

    def to_internal_value(self, data):
        internal_value = super().to_internal_value(data)
        apple_music_id = data.get("apple_music_id")
        internal_value.update({"apple_music_id": apple_music_id})
        return internal_value

    def create(self, validated_data):
        song = Album.objects.create(apple_music_id=validated_data.get("apple_music_id"))
        return song
