"""
Module contains serializers for favorites
"""
# pylint: disable=W0221

from api.albums.serializers import AlbumSerializer
from api.models.core import (
    Album,
    FavoritedAlbum,
    FavoritedPlaylist,
    FavoritedTrack,
    Playlist,
    Song,
    UserProfile,
)
from api.playlists.serializers import PlaylistSerializer
from api.songs.serializers import SongSerializer
from api.users.serializers import UserProfileSerializer
from django.db import transaction
from rest_framework import serializers


class FavoritedTrackSerializer(serializers.ModelSerializer):
    """
    Serializer for favorites
    """

    song = SongSerializer(read_only=True)
    favorite_type = serializers.SerializerMethodField()
    user = UserProfileSerializer(read_only=True)

    class Meta:
        """
        Serializer Meta Definition
        """

        model = FavoritedTrack
        fields = "__all__"

    def get_favorite_type(self, _):
        """
        Return favorite type
        """
        return "track"

    def validate(self, data):
        """
        Check if favorited_track already exists
        """
        if FavoritedTrack.objects.filter(
            user__auth0_user_id=data.get("auth0_user_id"),
            song__apple_music_id=data.get("apple_music_id"),
        ).count():
            raise serializers.ValidationError("Favorited Track Already Exists")
        return data

    def to_internal_value(self, data):
        internal_value = super(FavoritedTrackSerializer, self).to_internal_value(data)
        name = data.get("name")
        apple_music_id = data.get("apple_music_id")
        auth0_user_id = self.context.get("request").user
        internal_value.update(
            {
                "name": name,
                "apple_music_id": apple_music_id,
                "auth0_user_id": auth0_user_id,
            }
        )
        return internal_value

    @transaction.atomic
    def create(self, validated_data):
        song = Song.objects.get_or_create(
            name=validated_data.get("name"),
            apple_music_id=validated_data.get("apple_music_id"),
        )
        user = UserProfile.objects.get(
            auth0_user_id=validated_data.get("auth0_user_id")
        )
        return FavoritedTrack.objects.create(user=user, song=song)


class FavoritedAlbumSerializer(serializers.ModelSerializer):
    """
    Serializer for favorites
    """

    user = UserProfileSerializer(read_only=True)
    album = AlbumSerializer(read_only=True)
    favorite_type = serializers.SerializerMethodField()

    class Meta:
        """
        Serializer Meta Definition
        """

        model = FavoritedAlbum
        fields = ("user", "album", "favorite_type")

    def get_favorite_type(self, _):
        """
        Return favorite type
        """
        return "album"

    def to_internal_value(self, data):
        internal_value = super(FavoritedAlbumSerializer, self).to_internal_value(data)
        name = data.get("name")
        apple_music_id = data.get("apple_music_id")
        auth0_user_id = self.context.get("request").user
        internal_value.update(
            {
                "name": name,
                "apple_music_id": apple_music_id,
                "auth0_user_id": auth0_user_id,
            }
        )
        return internal_value

    @transaction.atomic
    def create(self, validated_data):
        album = Album.objects.get_or_create(
            name=validated_data.get("name"),
            apple_music_id=validated_data.get("apple_music_id"),
        )
        user = UserProfile.objects.get(
            auth0_user_id=validated_data.get("auth0_user_id")
        )
        return FavoritedTrack.objects.create(user=user, album=album)


class FavoritedPlaylistSerializer(serializers.ModelSerializer):
    """
    Serializer for favorites
    """

    user = UserProfileSerializer()
    playlist = PlaylistSerializer(read_only=True)
    favorite_type = serializers.SerializerMethodField()

    class Meta:
        """
        Serializer Meta Definition
        """

        model = FavoritedPlaylist
        fields = "__all__"

    def get_favorite_type(self, _):
        """
        Return favorite type
        """

        return "playlist"

    def to_internal_value(self, data):
        internal_value = super(FavoritedPlaylistSerializer, self).to_internal_value(
            data
        )
        name = data.get("name")
        apple_music_id = data.get("apple_music_id")
        auth0_user_id = self.context.get("request").user
        internal_value.update(
            {
                "name": name,
                "apple_music_id": apple_music_id,
                "auth0_user_id": auth0_user_id,
            }
        )
        return internal_value

    @transaction.atomic
    def create(self, validated_data):
        playlist = Playlist.objects.get_or_create(
            name=validated_data.get("name"),
            apple_music_id=validated_data.get("apple_music_id"),
        )
        user = UserProfile.objects.get(
            auth0_user_id=validated_data.get("auth0_user_id")
        )
        return FavoritedPlaylist.objects.get_or_create(user=user, playlist=playlist)


class FavoritedSerializer(serializers.ModelSerializer):
    """
    Serializer for favorites
    """

    @classmethod
    def get_serializer(cls, model):
        if model == FavoritedPlaylist:
            serializer = FavoritedPlaylistSerializer
        elif model == FavoritedTrack:
            serializer = FavoritedTrackSerializer
        else:
            serializer = FavoritedAlbumSerializer
        return serializer

    def to_representation(self, instance):
        serializer = self.get_serializer(instance.__class__)
        return serializer(instance, context=self.context).data

    class Meta:
        """
        Serializer Meta Definition
        """

        fields = "__all__"
