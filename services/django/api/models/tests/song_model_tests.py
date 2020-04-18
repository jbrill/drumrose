"""
Song Model Tests
"""

from api.models.core import Song
from api.models.factories import SongFactory
from django.test import TestCase


class SongTest(TestCase):
    """ Test module for Song """

    def test_get_single_song_simple(self):
        """
        Tests retrieving a song
        """
        SongFactory(name="Song Test")
        song = Song.objects.get(name="Song Test")
        self.assertEqual(song.albums.count(), 0)

    def test_get_multiple_songs_simple(self):
        """
        Tests creating and retrieving several simple songs
        """
        SongFactory.create_batch(25)
        self.assertEqual(Song.objects.count(), 25)
