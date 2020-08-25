"""
Favorites Serializers Test Module
"""

from api.favorites.serializers import (
    FavoritedAlbumSerializer,
    FavoritedPlaylistSerializer,
    FavoritedTrackSerializer,
)
from api.models.factories import (
    FavoritedAlbumFactory,
    FavoritedPlaylistFactory,
    FavoritedTrackFactory,
    SongFactory,
    UserProfileFactory,
)
from django.test import TestCase


class FavoritedTrackSerializerTest(TestCase):
    """
    Favorite Serializers Tests
    """

    def setUp(self):
        """
        Creates models on setup
        """
        self.user = UserProfileFactory.create(username="test_user")
        self.song = SongFactory.create(name="I Want You", apple_music_id="1422627289")

    def test_favorited_track_serializer_single(self):
        """
        Test single track serializer
        """
        favorited_track = FavoritedTrackFactory.create(user=self.user)

        # Do the serialization
        serialized_favorited_track = FavoritedTrackSerializer(
            favorited_track, many=False
        ).data

        # Assert favorited track fields
        self.assertEqual(
            serialized_favorited_track["song"]["apple_music_id"],
            str(favorited_track.song.apple_music_id),
        )
        self.assertEqual(serialized_favorited_track["user"]["username"], "test_user")

    def test_favorited_track_duplicate(self):
        """
        Test many track serializer
        """
        favorited_track_0 = FavoritedTrackFactory.create(user=self.user, song=self.song)
        favorited_track_1 = FavoritedTrackFactory.create(user=self.user, song=self.song)

        # Do the serialization
        serialized_favorited_tracks = FavoritedTrackSerializer(
            [favorited_track_0, favorited_track_1], many=True
        ).data

        # Assert favorited track fields
        self.assertEqual(
            serialized_favorited_tracks[0]["song"]["apple_music_id"],
            favorited_track_0.song.apple_music_id,
        )
        self.assertEqual(
            serialized_favorited_tracks[0]["user"]["username"], "test_user"
        )

    def test_favorited_album_serializer_single(self):
        """
        Test single album serializer
        """
        favorited_album = FavoritedAlbumFactory.create(user=self.user)

        # Do the serialization
        serialized_favorited_album = FavoritedAlbumSerializer(
            favorited_album, many=False
        ).data

        # Assert favorited track fields
        self.assertEqual(
            serialized_favorited_album["album"]["apple_music_id"],
            str(favorited_album.album.apple_music_id),
        )
        self.assertEqual(serialized_favorited_album["user"]["username"], "test_user")

    def test_favorited_playlist_serializer_single(self):
        """
        Test single playlist serializer
        """
        favorited_playlist = FavoritedPlaylistFactory.create(user=self.user)

        # Do the serialization
        serialized_favorited_playlist = FavoritedPlaylistSerializer(
            favorited_playlist, many=False
        ).data

        # Assert favorited track fields
        self.assertEqual(
            serialized_favorited_playlist["playlist"]["apple_music_id"],
            str(favorited_playlist.playlist.apple_music_id),
        )
        self.assertEqual(serialized_favorited_playlist["user"]["username"], "test_user")
