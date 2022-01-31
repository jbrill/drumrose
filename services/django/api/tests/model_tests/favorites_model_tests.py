"""
Favorites Model Tests
"""
from django.db import IntegrityError
from django.test import TestCase
from api.models.factories import FavoritedTrackFactory, SongFactory, UserProfileFactory


class FavoritesTest(TestCase):
    """
    Test module for Favorites
    """

    def setUp(self):
        """
        Creates user and track models on setup
        """
        self.user = UserProfileFactory.create(username="test_user")
        self.song = SongFactory.create(apple_music_id="1422627289")

    def test_create_favorited_track_already_exists_raises_exception(self):
        """
        Test many favorited tracks with same user and song raises
        an integrity error
        """
        with self.assertRaises(Exception) as raised:
            FavoritedTrackFactory.create_batch(2, user=self.user, song=self.song)
        self.assertEqual(IntegrityError, type(raised.exception))

    def test_create_favorited_track_simple(self):
        """
        Test simple favorited track success
        """
        favorited_track = FavoritedTrackFactory.create(user=self.user, song=self.song)
        self.assertEqual(favorited_track.user.id, self.user.id)
        self.assertEqual(favorited_track.song.id, self.song.id)
