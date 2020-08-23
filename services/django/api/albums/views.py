"""
Album route module
"""

import json

from api.albums.serializers import AlbumSerializer
from api.models.core import Album, FavoritedAlbum
from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView


class AlbumRoute(APIView):
    """
    API response for an artist
        GET: Retrieves an album
        POST: Creates an album
    """

    def get(self, request):
        """
        GET for  Artist
        """
        albums = Album.objects.all()
        serializer = AlbumSerializer(albums, many=True)
        return JsonResponse({"albums": serializer.data})

    def post(self, request):
        """
        POST for  Artist
        """
        artist_data = json.loads(request.body.decode("utf-8"))
        test_album = Album.objects.create(
            name=artist_data["name"], artwork_url=artist_data["url"]
        )
        serializer = AlbumSerializer(test_album)
        return JsonResponse(serializer.data)


class AlbumDetail(APIView):
    """
    Description:
        - API View for album Detail
    Routes:
        - GET /albums/:album_id/
            - Gets a album
        - PATCH /albums/:album_id
            - Updates a album
        - DELETE /albums/:album_id
            - Deletes a album
    """

    authentication_classes = []
    permission_classes = []

    def get(self, request, apple_music_id):
        try:
            album = Album.objects.get(apple_music_id=apple_music_id)
        except Album.DoesNotExist:
            return JsonResponse(
                {"message": "Song does not exist."}, status=status.HTTP_409_CONFLICT
            )

        print(album.page_id)
        is_favorited = False

        # HACK: checks if 'logged in' by checking request username
        if request.user.username:
            is_favorited = FavoritedAlbum.objects.filter(
                user=request.user, album=album
            ).exists()

        serializer = AlbumSerializer(album, context={"is_favorited": is_favorited})

        return JsonResponse({"track": serializer.data})

    def patch(self, request, post_id):
        """
        Update an album
        """
        print(post_id)
        pass

    def delete(self, request, post_id):
        """
        Delete an album
        """
        print(post_id)
        pass
