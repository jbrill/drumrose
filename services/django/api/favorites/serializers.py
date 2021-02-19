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
from rest_framework import serializers


class FavoritedTrackSerializer(serializers.ModelSerializer):
    """
    Serializer for favorites
    """

    song = SongSerializer(read_only=True)
    user = UserProfileSerializer(read_only=True)

    class Meta:
        """
        Serializer Meta Definition
        """

        model = FavoritedTrack
        fields = "__all__"

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
        song, _ = Song.objects.get_or_create(
            apple_music_id=validated_data.get("apple_music_id")
        )
        return FavoritedTrack.objects.create(user=user, song=song)


class FavoritedAlbumSerializer(serializers.ModelSerializer):
    """
    Serializer for favorites
    """

    album = AlbumSerializer(read_only=True)
    user = UserProfileSerializer(read_only=True)

    class Meta:
        """
        Serializer Meta Definition
        """

        model = FavoritedAlbum
        fields = "__all__"

    def validate(self, data):
        """
        Check if favorited album already exists
        """
        if FavoritedAlbum.objects.filter(
            user__auth0_user_id=data.get("auth0_user_id"),
            album__apple_music_id=data.get("apple_music_id"),
        ).count():
            print(data)
            raise serializers.ValidationError("Favorited Album Already Exists")
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
        return FavoritedAlbum.objects.create(user=user, album=album)


class FavoritedPlaylistSerializer(serializers.ModelSerializer):
    """
    Serializer for favorites
    """

    user = UserProfileSerializer(read_only=True)
    playlist = PlaylistSerializer(read_only=True)

    class Meta:
        """
        Serializer Meta Definition
        """

        model = FavoritedPlaylist
        fields = "__all__"

    def validate(self, data):
        """
        Check if favorited_track already exists
        """
        if FavoritedPlaylist.objects.filter(
            user__auth0_user_id=data.get("auth0_user_id"),
            playlist__apple_music_id=data.get("apple_music_id"),
        ).count():
            raise serializers.ValidationError("Favorited Playlist Already Exists")
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
        playlist, _ = Playlist.objects.get_or_create(
            apple_music_id=validated_data.get("apple_music_id")
        )
        return FavoritedPlaylist.objects.create(user=user, playlist=playlist)
