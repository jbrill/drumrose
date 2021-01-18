from api.models.core import FavoritedTrack, Song, TrackReview
from api.services.apple_music import get_track_info
from rest_framework import serializers
from django.db import transaction


class SongSerializer(serializers.ModelSerializer):

    favorited = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Song
        fields = "__all__"

    def get_favorited(self, obj):
        auth0_user_id = str(self.context.get("request").user).replace(".", "|")
        print(auth0_user_id)
        print(self.context.get("request").user)
        print(obj.apple_music_id)
        print(
            FavoritedTrack.objects.filter(
                user__auth0_user_id=auth0_user_id,
                song__apple_music_id=obj.apple_music_id,
            ).exists()
        )
        return FavoritedTrack.objects.filter(
            user__auth0_user_id=auth0_user_id, song__apple_music_id=obj.apple_music_id
        ).exists()

    def validate(self, data):
        """
        Check if favorited_track already exists
        """
        if Song.objects.filter(song__apple_music_id=data.get("apple_music_id")).count():
            raise serializers.ValidationError("Song Already Exists")
        return data

    def to_internal_value(self, data):
        internal_value = super().to_internal_value(data)
        name = data.get("name")
        apple_music_id = data.get("apple_music_id")
        internal_value.update({"name": name, "apple_music_id": apple_music_id})
        return internal_value

    @transaction.atomic
    def create(self, validated_data):
        song = Song.objects.create(
            name=validated_data.get("name"),
            apple_music_id=validated_data.get("apple_music_id"),
        )
        return song
