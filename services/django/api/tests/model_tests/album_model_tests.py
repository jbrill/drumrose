"""
Album Models Tests
"""
from django.test import TestCase
from api.models.core import Album
from api.models.factories import AlbumFactory


class AlbumTest(TestCase):
    """ Test module for Album """

    def test_get_single_album_simple(self):
        """
        Tests retrieving a single album
        """
        album = AlbumFactory()
        self.assertTrue(Album.objects.count(), 25)
        self.assertIsInstance(album, Album)

    def test_get_multiple_albums_simple(self):
        """
        Tests creating and retreiving several simple album objects
        """
        AlbumFactory.create_batch(25)
        self.assertTrue(Album.objects.count(), 25)
