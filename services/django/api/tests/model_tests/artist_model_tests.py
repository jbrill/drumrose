"""
Artist Model Tests
"""
from django.test import TestCase
from api.models.core import Artist
from api.models.factories import ArtistFactory


class ArtistTest(TestCase):
    """
    Test module for Artist
    """

    def test_get_single_artist_simple(self):
        """
        Tests retrieving a artist
        """
        ArtistFactory()
        self.assertEqual(Artist.objects.count(), 1)
        self.assertIsInstance(Artist.objects.first().apple_music_id, str)

    def test_get_multiple_artists_simple(self):
        """
        Tests retrieving a artist
        """
        ArtistFactory.create_batch(25)
        self.assertEqual(Artist.objects.count(), 25)
