"""
Album Views Tests
"""

from api.models.factories import AlbumFactory
from django.test import TestCase
from django.urls import reverse


class AlbumViewTest(TestCase):
    """ Test module for Album Views """

    def test_get_albums(self):
        """
        Tests retrieving album list view
        """
        test_album = AlbumFactory(name="Test Album")
        url = reverse("AlbumsRoute")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.json()["albums"]), 1)
        self.assertEqual(resp.json()["albums"][0]["name"], test_album.name)
