"""
Song Model Tests
"""
from django.test import TestCase
from api.models.core import Song
from api.models.factories import SongFactory


class SongTest(TestCase):
    """ Test module for Song """

    def test_get_single_song_simple(self):
        """
        Tests retrieving a song
        """
        SongFactory(name="Song Test")
        self.assertEqual(Song.objects.count(), 1)
        self.assertEqual(Song.objects.first().name, "Song Test")

    def test_get_multiple_songs_simple(self):
        """
        Tests creating and retrieving several simple songs
        """
        SongFactory.create_batch(25)
        self.assertEqual(Song.objects.count(), 25)
