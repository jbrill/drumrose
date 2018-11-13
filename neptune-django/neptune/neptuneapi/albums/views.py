from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from neptuneapi.albums.serializers import AlbumSerializer
from neptuneapi.models.neptune_core import NeptuneAlbum

import json

@csrf_exempt
def NeptuneAlbumRoute(request):
    """
    API response for an artist
        GET: Retrieves an album
        POST: Creates an album
    """
    if request.method == "GET":
        albums = NeptuneALbum.objects.all()
        return JsonResponse(albums)
    if request.method == "POST":
        artist_data = json.loads(request.body.decode('utf-8'))
        print(artist_data)
        test_album = NeptuneAlbum.objects.create(
            name=artist_data["name"],
            artwork_url=artist_data["url"]
        )
        serializer = AlbumSerializer(test_album)
        return JsonResponse(serializer.data)
