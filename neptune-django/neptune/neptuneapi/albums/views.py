from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from neptuneapi.albums.serializers import AlbumSerializer
from neptuneapi.models.neptune_core import NeptuneAlbum

@csrf_exempt
def NeptuneAlbumRoute(request):
    """
    API response for an artist
        GET: Retrieves an album
        POST: Creates an album
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
        test_album = NeptuneAlbum.objects.create(
            name="test_album",
            artwork_url="https://upload.wikimedia.org/wikipedia/en/thumb/0/0f/Radiohead.pablohoney.albumart.jpg/220px-Radiohead.pablohoney.albumart.jpg"
        )
        print(test_album)
        artist = {
            "test_name": "test",
        }
        serializer = AlbumSerializer(test_album)
        return JsonResponse(serializer.data)
