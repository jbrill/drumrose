from api.models.core import Song
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

    def get_favorited(self, _):
        return self.context.get("is_favorited") or False
