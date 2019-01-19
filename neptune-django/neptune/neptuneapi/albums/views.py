"""
Album route module
"""

import json

from django.http import JsonResponse

from neptuneapi.albums.serializers import AlbumSerializer
from neptuneapi.models.neptune_core import NeptuneAlbum

from rest_framework.views import APIView


class NeptuneAlbumRoute(APIView):
    """
    API response for an artist
        GET: Retrieves an album
        POST: Creates an album
    """

    def get(self):
        """
        GET for Neptune Artist
        """
        albums = NeptuneAlbum.objects.all()
        return JsonResponse(albums)

    def post(self, request):
        """
        POST for Neptune Artist
        """
        artist_data = json.loads(request.body.decode('utf-8'))
        print(artist_data)
        test_album = NeptuneAlbum.objects.create(
            name=artist_data["name"],
            artwork_url=artist_data["url"]
        )
        serializer = AlbumSerializer(test_album)
        return JsonResponse(serializer.data)
