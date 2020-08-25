import json

from api.favorites.serializers import (
    FavoritedAlbumSerializer,
    FavoritedPlaylistSerializer,
    FavoritedTrackSerializer,
)
from api.favorites.views import FavoritesList, FavoriteTracksList
from api.models.core import FavoritedAlbum, FavoritedPlaylist, FavoritedTrack
from api.models.factories import (
    AlbumFactory,
    FavoritedAlbumFactory,
    FavoritedPlaylistFactory,
    FavoritedTrackFactory,
    PlaylistFactory,
    SongFactory,
    UserProfileFactory,
)
from api.tests.api_tests.util import get_test_token
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIRequestFactory

factory = APIRequestFactory()


class FavoritesTest(TestCase):
    """
    Test cases for favorites views
    """

    def setUp(self):
        """
        Creates models on setup
        """
        self.token = json.loads(get_test_token())["access_token"]
        test_username = "test_username"
        test_auth0_user_id = "ApqgC9UHWyDV0Qb6rv3cby0gP47u5ZmO@clients"

        self.user = UserProfileFactory.create(
            auth0_user_id=test_auth0_user_id, username=test_username
        )
        self.song = SongFactory.create()
        self.album = AlbumFactory.create()
        self.playlist = PlaylistFactory.create()

        self.favorited_track = FavoritedTrackFactory.create(
            user=self.user, song=self.song
        )
        self.favorited_album = FavoritedAlbumFactory.create(
            user=self.user, album=self.album
        )
        self.favorited_playlist = FavoritedPlaylistFactory.create(
            user=self.user, playlist=self.playlist
        )

    def test_get_all_favorites(self):
        view = FavoritesList.as_view()
        request = factory.get(
            reverse("FavoritesList"),
            content_type="application/json",
            data={},
            HTTP_AUTHORIZATION="Bearer " + self.token,
        )
        response = view(request)
        favorited_response = json.loads(response.content)
        favorited_track = FavoritedTrack.objects.get(id=self.favorited_track.id)
        serializer = FavoritedTrackSerializer(favorited_track)
        self.assertEqual(
            favorited_response[0]["user"]["username"],
            serializer.data["user"].get("username"),
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_track_favorites(self):
        view = FavoriteTracksList.as_view()
        request = factory.get(
            reverse("FavoriteTracksList"),
            content_type="application/json",
            data={},
            HTTP_AUTHORIZATION="Bearer " + self.token,
        )
        response = view(request)
        favorited_track = FavoritedTrack.objects.get(id=self.favorited_track.id)
        serializer = FavoritedTrackSerializer(favorited_track)
        favorited_track_response = json.loads(response.content)
        self.assertEqual(
            favorited_track_response[0]["user"]["username"],
            serializer.data["user"].get("username"),
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_album_favorites(self):
        response = factory.get(
            reverse("FavoriteAlbumsList"),
            content_type="application/json",
            data={},
            HTTP_AUTHORIZATION="Bearer " + self.token,
        )
        favorited_album = FavoritedAlbum.objects.get(id=self.favorited_album.id)
        serializer = FavoritedAlbumSerializer(favorited_album)
        favorited_album_response = response.json()

        self.assertEqual(
            favorited_album_response[0]["user"]["username"],
            serializer.data["user"].get("username"),
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_playlist_favorites(self):
        response = factory.get(
            reverse("FavoritePlaylistsList"),
            content_type="application/json",
            data={},
            HTTP_AUTHORIZATION="Bearer " + self.token,
        )
        favorited_playlist = FavoritedPlaylist.objects.get(
            id=self.favorited_playlist.id
        )
        serializer = FavoritedPlaylistSerializer(favorited_playlist)
        favorited_playlist_response = response.json()
        self.assertEqual(
            favorited_playlist_response[0]["user"]["username"],
            serializer.data["user"].get("username"),
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_invalid_favorited_track_duplicate(self):
        view = FavoriteTracksList.as_view()
        request = factory.post(
            reverse("FavoriteTracksList"),
            content_type="application/json",
            data={"track_id": self.favorited_track.id, "track_name": "test"},
            HTTP_AUTHORIZATION="Bearer " + self.token,
        )
        response = view(request)
        print(response)
        favorited_track = FavoritedTrack.objects.get(id=self.favorited_track.id)
        serializer = FavoritedTrackSerializer(favorited_track)
        print(response.content)
        favorited_track_response = json.loads(response.content)
        self.assertEqual(
            favorited_track_response[0]["user"]["username"],
            serializer.data["user"].get("username"),
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
