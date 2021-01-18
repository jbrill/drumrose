"""
Reviews Serializers Test Module
"""

from api.models.factories import (
    AlbumFactory,
    AlbumReviewFactory,
    SongFactory,
    TrackReviewFactory,
    UserProfileFactory,
)
from api.reviews.serializers import AlbumReviewSerializer, TrackReviewSerializer
from django.test import TestCase


class ReviewSerializersTests(TestCase):
    """
    Review Serializer Tests
    """

    def setUp(self):
        """
        Creates models on setup
        """
        self.user = UserProfileFactory.create(username="test_user")
        self.album = AlbumFactory.create(name="I Want You", apple_music_id="1422627289")
        self.track = SongFactory.create(name="I Want You", apple_music_id="1422627289")

    def test_album_review_serializer_single(self):
        """
        Test single album review serializer
        """
        reviewed_album = AlbumReviewFactory.create(user=self.user)

        serialized_album_review = AlbumReviewSerializer(reviewed_album, many=False).data

        self.assertEqual(
            serialized_album_review["album"]["apple_music_id"],
            str(reviewed_album.album.apple_music_id),
        )
        self.assertEqual(
            serialized_album_review["user"]["username"], self.user.username
        )

    def test_track_review_serializer_single(self):
        """
        Test single album review serializer
        """
        reviewed_track = TrackReviewFactory(
            user=self.user, track=self.track, review=None, rating="0.5"
        )
        serialized_track_review = TrackReviewSerializer(reviewed_track, many=False)
        self.assertEqual(
            serialized_track_review["track"]["apple_music_id"].value,
            self.track.apple_music_id,
        )
        self.assertEqual(
            serialized_track_review["user"]["username"].value, self.user.username
        )
        self.assertEqual(serialized_track_review["rating"].value, "0.5")
