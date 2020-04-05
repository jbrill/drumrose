"""
Artist Route Module
"""

from django.http import JsonResponse
from rest_framework.views import APIView

from api.artists.serializers import ArtistSerializer
from api.models.core import Artist


class ArtistRoute(APIView):
    """
    API response for an artist
        GET: Retrieves an artist
        POST: Creates an artist
    """

    def get(self, request):
        """
         Artist GET
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
         Artist POST
        """
        test_artist = Artist.objects.create(
            name="test"
        )
        serializer = ArtistSerializer(test_artist)
        return JsonResponse(serializer.data)
