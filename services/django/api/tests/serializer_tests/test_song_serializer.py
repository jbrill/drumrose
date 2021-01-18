"""
Song Serializer Test Module
"""

from api.models.factories import SongFactory, TrackReviewFactory
from api.songs.serializers import SongSerializer
from django.test import TestCase
from rest_framework.test import APIRequestFactory


class SongSerializerTest(TestCase):
    """
    Song Serializer Test
    """

    def test_song_serializer(self):
        """
        Test single song serializer
        """

        request = APIRequestFactory().request()
        # request.user = user
        song = SongFactory(apple_music_id="1422627289", name="I Want You")

        # Do the serialization
        serialized_song = SongSerializer(
            song, many=False, context={"request": request}
        ).data

        # Assert song fields
        self.assertEqual(serialized_song["apple_music_id"], str(song.apple_music_id))
        self.assertIn("reviews", serialized_song)
