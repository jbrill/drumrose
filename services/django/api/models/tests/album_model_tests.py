"""
Album Models Tests
"""

from api.models.core import Album
from api.models.factories import AlbumFactory
from django.test import TestCase


class AlbumTest(TestCase):
    """ Test module for Album """

    def test_get_single_album_simple(self):
        """
        Tests retrieving a single album
        """
        AlbumFactory(name="Test Album",)
        test_album = Album.objects.get(name="Test Album")
        self.assertEqual(test_album.artwork_url, "test_url")

    def test_get_multiple_albums_simple(self):
        """
        Tests creating and retreiving several simple album objects
        """
        AlbumFactory.create_batch(25)
        self.assertTrue(Album.objects.count(), 25)
