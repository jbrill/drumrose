"""
Album Views
"""

from api.albums.serializers import AlbumSerializer
from api.models.core import Album
from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_auth0.authentication import Auth0JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class AlbumRoute(APIView):
    """
    API response for an artist
        GET: Retrieves an album
        POST: Creates an album
    """

    authentication_classes = [Auth0JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        """
        GET for album
        """
        albums = Album.objects.all().order_by("?")
        return JsonResponse(
            {"albums": list(albums.values())}, status=status.HTTP_200_OK
        )

    def post(self, request):
        """
        Create an artist
        """
        serializer = AlbumSerializer(data={"apple_music_id": request.data["id"]})
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(
                serializer.data, status=status.HTTP_201_CREATED, safe=False
            )
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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

    authentication_classes = [Auth0JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, album_id):
        """
        Album Detail View
        """
        try:
            album = Album.objects.get(apple_music_id=album_id)
        except Album.DoesNotExist:
            return JsonResponse(
                {"message": "Album does not exist."}, status=status.HTTP_409_CONFLICT
            )

        serializer = AlbumSerializer(album, context={"request": request})
        return JsonResponse({"album": serializer.data})

    def patch(self, request, album_id):
        """
        Update an album
        """
        print(album_id)
        return JsonResponse({})

    def delete(self, request, album_id):
        """
        Delete an album
        """
        print(album_id)
        return JsonResponse({})
