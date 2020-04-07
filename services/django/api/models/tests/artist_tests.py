"""
Artist Model Tests
"""

from api.models.core import Artist
from api.models.factories import ArtistFactory
from django.test import TestCase


class ArtistTest(TestCase):
    """ Test module for Artist """

    def test_get_single_artist_simple(self):
        """
        Tests retrieving a artist
        """
        ArtistFactory(name="Casper")
        casper = Artist.objects.get(name="Casper")
        self.assertEqual(casper.songs.count(), 0)

    def test_get_multiple_artists_simple(self):
        """
        Tests retrieving a artist
        """
        ArtistFactory.create_batch(25)
        self.assertEqual(Artist.objects.count(), 25)
