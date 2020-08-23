"""
Song Serializer Test Module
"""

from api.models.factories import SongFactory
from api.songs.serializers import SongSerializer
from django.test import TestCase


class SongSerializerTest(TestCase):
    """
    Song Serializer Test
    """

    def test_song_serializer(self):
        """
        Test single song serializer
        """
        song = SongFactory(apple_music_id="1422627289")

        # Do the serialization
        serialized_song = SongSerializer(song, many=False).data

        # Assert album fields
        self.assertEqual(serialized_song["apple_music_id"], str(song.apple_music_id))
