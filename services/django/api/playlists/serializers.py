"""
Module contains playlist serializers
"""

from api.models.core import Playlist, FavoritedPlaylist, PlaylistReview
from rest_framework import serializers
from django.db.models import Avg


class PlaylistSerializer(serializers.ModelSerializer):

    favorited = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Playlist
        fields = "__all__"

    def get_review_summary(self, obj):
        playlist_reviews = PlaylistReview.objects.filter(
            playlist__apple_music_id=obj.apple_music_id
        )
        review_count = playlist_reviews.count()
        average_review = playlist_reviews.aggregate(Avg("rating"))
        return {
            "total_reviews": review_count,
            "average_review": average_review.get("rating__avg"),
            "totals_per_rating": {
                "0.0": playlist_reviews.filter(rating=0.0).count(),
                "0.5": playlist_reviews.filter(rating=0.5).count(),
                "1.0": playlist_reviews.filter(rating=1.0).count(),
                "1.5": playlist_reviews.filter(rating=1.5).count(),
                "2.0": playlist_reviews.filter(rating=2.0).count(),
                "2.5": playlist_reviews.filter(rating=2.5).count(),
                "3.0": playlist_reviews.filter(rating=3.0).count(),
                "3.5": playlist_reviews.filter(rating=3.5).count(),
                "4.0": playlist_reviews.filter(rating=4.0).count(),
                "4.5": playlist_reviews.filter(rating=4.5).count(),
                "5.0": playlist_reviews.filter(rating=5.0).count(),
            },
        }

    def get_favorited(self, obj):
        if "request" not in self.context:
            return False
        auth0_user_id = str(self.context.get("request").user).replace(".", "|")
        return FavoritedPlaylist.objects.filter(
            user__auth0_user_id=auth0_user_id,
            playlist__apple_music_id=obj.apple_music_id,
        ).exists()

    def validate(self, data):
        """
        Check if favorited_track already exists
        """
        if Playlist.objects.filter(apple_music_id=data.get("apple_music_id")).count():
            raise serializers.ValidationError("Playlist Already Exists")
        return data

    def to_internal_value(self, data):
        internal_value = super().to_internal_value(data)
        apple_music_id = data.get("apple_music_id")
        internal_value.update({"apple_music_id": apple_music_id})
        return internal_value

    def create(self, validated_data):
        playlist = Playlist.objects.create(
            apple_music_id=validated_data.get("apple_music_id")
        )
        return playlist
