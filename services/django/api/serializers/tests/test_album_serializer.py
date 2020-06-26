"""
Album Serializer Test Module
"""

from api.albums.serializers import AlbumSerializer
from api.models.factories import AlbumFactory
from django.test import TestCase


class AlbumSerializerTest(TestCase):
    """
    Album Serializer Test
    """

    def test_album_serializer(self):
        """
        Test single album serializer
        """
        album = AlbumFactory()

        # Do the serialization
        serialized_album = AlbumSerializer(album, many=False).data

        # Assert album fields
        self.assertEqual(
            serialized_album["apple_music_id"], str(album.apple_music_id)
        )
