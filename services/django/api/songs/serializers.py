from api.models.core import FavoritedTrack, Song
from api.services.apple_music import get_track_info
from rest_framework import serializers


class SongSerializer(serializers.ModelSerializer):
    attributes = serializers.SerializerMethodField()
    favorited = serializers.SerializerMethodField()

    class Meta:
        model = Song
        fields = "__all__"

    def get_attributes(self, obj):
        return get_track_info(obj.apple_music_id)

    def get_favorited(self, obj):
        if "request" not in self.context or "user" not in self.context.get("request"):
            return False
        return FavoritedTrack.objects.filter(
            user__auth0_user_id=self.context["request"].user,
            song__apple_music_id=obj.apple_music_id,
        ).exists()
