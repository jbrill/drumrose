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

        # request = APIRequestFactory().request()
        # request.user = user
        song = SongFactory(apple_music_id="1422627289", name="I Want You")

        # Do the serialization
        serialized_song = SongSerializer(song, many=False).data

        # Assert song fields
        self.assertEqual(serialized_song["apple_music_id"], str(song.apple_music_id))
        self.assertIn("review_summary", serialized_song)

    def test_song_serializer_multiple_reviews(self):
        """
        Tests Song Serializer With Reviews
        """
        song = SongFactory(apple_music_id="1422627289", name="I Want You")

        TrackReviewFactory.create_batch(5, track=song)
        serialized_song = SongSerializer(song, many=False).data

        # Assert song fields
        self.assertEqual(serialized_song["apple_music_id"], str(song.apple_music_id))
        self.assertEqual(5, serialized_song["review_summary"]["total_reviews"])
        self.assertEqual(
            5, serialized_song["review_summary"]["totals_per_rating"]["0.5"]
        )
