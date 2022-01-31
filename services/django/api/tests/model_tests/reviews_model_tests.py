"""
Reviews Model Tests
"""
from django.db import IntegrityError
from django.test import TestCase
from api.models.factories import SongFactory, TrackReviewFactory, UserProfileFactory


class ReviewsTest(TestCase):
    """
    Test module for Reviews
    """

    def setUp(self):
        """
        Creates models on setup
        """
        self.user = UserProfileFactory.create(username="test_user")
        self.song = SongFactory.create(apple_music_id="1422627289")

    def test_create_track_review_already_exists_raises_exception(self):
        """
        Test two track reviews with same track and user raises
        integrity error
        """
        with self.assertRaises(Exception) as raised:
            TrackReviewFactory.create_batch(2, user=self.user, track=self.song)
        self.assertEqual(IntegrityError, type(raised.exception))

    def test_create_track_review_simple(self):
        """
        Test create simple track review succeeds
        """
        track_review = TrackReviewFactory.create(user=self.user, track=self.song)
        self.assertEqual(track_review.user.id, self.user.id)
        self.assertEqual(track_review.track.id, self.song.id)
