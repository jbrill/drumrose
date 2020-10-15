import json

from api.models.core import AlbumReview, PlaylistReview, TrackReview
from api.models.factories import (
    AlbumFactory,
    AlbumReviewFactory,
    PlaylistFactory,
    PlaylistReviewFactory,
    SongFactory,
    TrackReviewFactory,
    UserProfileFactory,
)
from api.reviews.serializers import (
    AlbumReviewSerializer,
    PlaylistReviewSerializer,
    TrackReviewSerializer,
)
from api.reviews.views import (
    AlbumReviewList,
    PlaylistReviewList,
    ReviewsList,
    TrackReviewList,
)
from api.tests.api_tests.util import ACCESS_TOKEN, get_test_token
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient


class ReviewsTest(TestCase):
    """
    Test cases for favorites views
    """

    def setUp(self):
        """
        Creates models on setup
        """
        # self.token = json.loads(get_test_token())["access_token"]
        self.token = ACCESS_TOKEN
        self.cleint = APIClient()

        test_username = "test_username"
        test_auth0_user_id = "ApqgC9UHWyDV0Qb6rv3cby0gP47u5ZmO@clients"

        self.user = UserProfileFactory.create(
            auth0_user_id=test_auth0_user_id, username=test_username
        )
        self.song = SongFactory.create()
        self.album = AlbumFactory.create()
        self.playlist = PlaylistFactory.create()

        self.reviewed_track = TrackReviewFactory.create(user=self.user, track=self.song)
        self.reviewed_album = AlbumReviewFactory.create(
            user=self.user, album=self.album
        )
        self.reviewed_playlist = PlaylistReviewFactory.create(
            user=self.user, playlist=self.playlist
        )

    def test_get_all_reviews(self):
        response = self.client.get(
            reverse("ReviewsList"),
            content_type="application/json",
            data={},
            HTTP_AUTHORIZATION="Bearer " + self.token,
        )
        reviews_response = json.loads(response.content)
        reviewed_track = TrackReview.objects.get(id=self.reviewed_track.id)
        serializer = TrackReviewSerializer(reviewed_track)
        self.assertEqual(
            reviews_response["reviews"][0]["user"]["username"],
            serializer.data["user"].get("username"),
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_track_reviews(self):
        response = self.client.get(
            reverse("TrackReviewList"),
            content_type="application/json",
            data={},
            HTTP_AUTHORIZATION="Bearer " + self.token,
        )
        reviewed_track = TrackReview.objects.get(id=self.reviewed_track.id)
        serializer = TrackReviewSerializer(reviewed_track)
        reviewed_track_response = json.loads(response.content)
        print(reviewed_track_response)
        self.assertEqual(
            reviewed_track_response["track_reviews"][0]["user"]["username"],
            serializer.data["user"].get("username"),
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_album_reviews(self):
        response = self.client.get(
            reverse("AlbumReviewList"),
            content_type="application/json",
            data={},
            HTTP_AUTHORIZATION="Bearer " + self.token,
        )
        reviewed_album = AlbumReview.objects.get(id=self.reviewed_album.id)
        serializer = AlbumReviewSerializer(reviewed_album)
        reviewed_album_response = response.json()

        self.assertEqual(
            reviewed_album_response["album_reviews"][0]["user"]["username"],
            serializer.data["user"].get("username"),
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_playlist_reviews(self):
        response = self.client.get(
            reverse("PlaylistReviewList"),
            content_type="application/json",
            data={},
            HTTP_AUTHORIZATION="Bearer " + self.token,
        )
        reviewed_playlist = PlaylistReview.objects.get(id=self.reviewed_playlist.id)
        serializer = PlaylistReviewSerializer(reviewed_playlist)
        reviewed_playlist_response = response.json()
        self.assertEqual(
            reviewed_playlist_response["playlist_reviews"][0]["user"]["username"],
            serializer.data["user"].get("username"),
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_invalid_reviewed_track_duplicate(self):
        response = self.client.post(
            reverse("TrackReviewList"),
            content_type="application/json",
            data=json.dumps(
                {
                    "apple_music_id": self.reviewed_track.track.apple_music_id,
                    "name": "test",
                }
            ),
            HTTP_AUTHORIZATION="Bearer " + self.token,
        )

        reviewed_track_response = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            reviewed_track_response.get("non_field_errors")[0],
            "Favorited Track Already Exists",
        )
