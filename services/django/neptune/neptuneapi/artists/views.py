"""
Artist Route Module
"""

from django.http import JsonResponse
from rest_framework.views import APIView

from neptuneapi.artists.serializers import ArtistSerializer
from neptuneapi.models.neptune_core import NeptuneArtist


class NeptuneArtistRoute(APIView):
    """
    API response for an artist
        GET: Retrieves an artist
        POST: Creates an artist
    """

    def get(self, request):
        """
        Neptune Artist GET
        """
        artist_1 = {
            "name": "Dr. Dre",
        }

        artists = {
            "artists": [
                artist_1
            ]
        }
        return JsonResponse(artists)

    def post(self, request):
        """
        Neptune Artist POST
        """
        test_artist = NeptuneArtist.objects.create(
            name="test"
        )
        serializer = ArtistSerializer(test_artist)
        return JsonResponse(serializer.data)