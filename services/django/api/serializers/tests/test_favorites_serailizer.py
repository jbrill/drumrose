"""
Favorites Serializers Test Module
"""
from unittest.mock import Mock, patch

from api.favorites.serializers import FavoritedTrackSerializer
from api.models.factories import FavoritedTrackFactory
from django.test import TestCase


class FavoritedTrackSerializerTest(TestCase):
    """
    Album Serializer Test
    """

    @patch("api.favorites.serializers.FavoritedTrackSerializer.get_user")
    def test_favorited_track_serializer(self, mock_user):
        """
        Test single album serializer
        """
        mock_user.return_value = {"name": "test_user"}

        favorited_track = FavoritedTrackFactory()

        # Do the serialization
        serialized_favorited_track = FavoritedTrackSerializer(
            favorited_track, many=False
        ).data

        # Assert favorited track fields
        self.assertEqual(
            serialized_favorited_track["song"]["apple_music_id"],
            str(favorited_track.song.apple_music_id),
        )
        self.assertEqual(
            serialized_favorited_track["user"]["name"], "test_user",
        )
