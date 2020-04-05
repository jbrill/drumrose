"""
Album route module
"""

import json

from django.http import JsonResponse

from api.albums.serializers import AlbumSerializer
from api.models.core import Album

from rest_framework.views import APIView


class AlbumRoute(APIView):
    """
    API response for an artist
        GET: Retrieves an album
        POST: Creates an album
    """

    def get(self):
        """
        GET for  Artist
        """
        albums = Album.objects.all()
        return JsonResponse(albums)

    def post(self, request):
        """
        POST for  Artist
        """
        artist_data = json.loads(request.body.decode('utf-8'))
        print(artist_data)
        test_album = Album.objects.create(
            name=artist_data["name"],
            artwork_url=artist_data["url"]
        )
        serializer = AlbumSerializer(test_album)
        return JsonResponse(serializer.data)
