from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from neptuneapi.artists.serializers import ArtistSerializer
from neptuneapi.models.neptune_core import NeptuneArtist

@csrf_exempt
def NeptuneArtistRoute(request):
    """
    API response for an artist
        GET: Retrieves an artist
        POST: Creates an artist
    """

    if request.method == "GET":
        artist_1 = {
            "name": "Dr. Dre",
        }

        artists = {
            "artists": [
                artist_1
            ]
        }
        return JsonResponse(artists)
    if request.method == "POST":
        test_artist = NeptuneArtist.objects.create(
            name="test"
        )
        print(test_artist)
        artist = {
            "test_name": "test",
        }
        serializer = ArtistSerializer(test_artist)
        return JsonResponse(serializer.data)
