from api.models.core import FavoritedTrack, Song, TrackReview
from rest_framework import serializers
from django.db.models import Avg


class SongSerializer(serializers.ModelSerializer):

    favorited = serializers.SerializerMethodField(read_only=True)
    review_summary = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Song
        fields = "__all__"

    def get_review_summary(self, obj):
        track_reviews = TrackReview.objects.filter(
            track__apple_music_id=obj.apple_music_id
        )
        review_count = track_reviews.count()
        average_review = track_reviews.aggregate(Avg("rating"))
        return {
            "total_reviews": review_count,
            "average_review": average_review.get("rating__avg"),
            "totals_per_rating": {
                "0.0": track_reviews.filter(rating=0.0).count(),
                "0.5": track_reviews.filter(rating=0.5).count(),
                "1.0": track_reviews.filter(rating=1.0).count(),
                "1.5": track_reviews.filter(rating=1.5).count(),
                "2.0": track_reviews.filter(rating=2.0).count(),
                "2.5": track_reviews.filter(rating=2.5).count(),
                "3.0": track_reviews.filter(rating=3.0).count(),
                "3.5": track_reviews.filter(rating=3.5).count(),
                "4.0": track_reviews.filter(rating=4.0).count(),
                "4.5": track_reviews.filter(rating=4.5).count(),
                "5.0": track_reviews.filter(rating=5.0).count(),
            },
        }

    def get_favorited(self, obj):
        if "request" not in self.context:
            return False
        try:
            auth0_user_id = str(self.context.get("request").user).split(".")[1]
        except IndexError:
            return False
        return FavoritedTrack.objects.filter(
            user__auth0_user_id=auth0_user_id, song__apple_music_id=obj.apple_music_id
        ).exists()

    # pylint: disable=W0221
    def validate(self, data):
        """
        Check if favorited_track already exists
        """
        # TODO: Check if you can get song with apple music api
        if Song.objects.filter(apple_music_id=data.get("apple_music_id")).count():
            raise serializers.ValidationError("Song Already Exists")
        return data

    def to_internal_value(self, data):
        internal_value = super().to_internal_value(data)
        name = data.get("name")
        apple_music_id = data.get("apple_music_id")
        internal_value.update({"name": name, "apple_music_id": apple_music_id})
        return internal_value

    def create(self, validated_data):
        song = Song.objects.create(apple_music_id=validated_data.get("apple_music_id"))
        return song
