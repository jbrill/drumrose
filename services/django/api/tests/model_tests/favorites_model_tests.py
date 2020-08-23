"""
Favorites Model Tests
"""

from api.models.factories import FavoritedTrackFactory, SongFactory, UserProfileFactory
from django.db import IntegrityError
from django.test import TestCase


class FavoritesTest(TestCase):
    """
    Test module for Favorites
    """

    def setUp(self):
        """
        Creates models on setup
        """
        self.user = UserProfileFactory.create(username="test_user")
        self.song = SongFactory.create(apple_music_id="1422627289")

    def test_create_favorited_track_already_exists_raises_exception(self):
        """
        Test many track serializer
        """
        with self.assertRaises(Exception) as raised:
            FavoritedTrackFactory.create_batch(2, user=self.user, song=self.song)
        self.assertEqual(IntegrityError, type(raised.exception))
