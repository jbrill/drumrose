"""
Playlist Route Definition
"""
# pylint: disable=W0612,W0613

from api.models.core import FavoritedPlaylist, Playlist
from api.playlists.serializers import PlaylistSerializer
from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_auth0.authentication import Auth0JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


class PlaylistList(APIView):
    """
    Description:
        - API View for Playlist List
    Routes:
        - GET /playlists/
            - Gets a list of playlists
        - POST /playlists/
            - Creates a new playlist
    """

    authentication_classes = [Auth0JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        """
        Returns a list of playlists
        """
        playlists = Playlist.objects.all()

        return JsonResponse(
            {"playlists": list(playlists.values())}, status=status.HTTP_200_OK
        )

    def post(self, request):
        """
        Returns a 201 if successful
        """
        serializer = PlaylistSerializer(
            data={"apple_music_id": request.data["id"], "name": request.data["name"]}
        )
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(
                serializer.data, status=status.HTTP_201_CREATED, safe=False
            )
        print(serializer.errors)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PlaylistDetail(APIView):
    """
    Description:
        - API View for Playlist Detail
    Routes:
        - GET /playlists/:playlist_id
            - Gets a post
        - PATCH /playlists/:playlist_id
            - Updates a post
        - DELETE /playlists/:playlist_id
            - Deletes a post
    """

    authentication_classes = [Auth0JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, playlist_id):
        """
        Returns a serialized playlist
        """
        try:
            playlist = Playlist.objects.get(apple_music_id=playlist_id)
        except Playlist.DoesNotExist:
            return JsonResponse(
                {"message": "Playlist does not exist."}, status=status.HTTP_409_CONFLICT
            )

        serializer = PlaylistSerializer(playlist, context={"request": request})
        return JsonResponse({"playlist": serializer.data})

    def patch(self, request, playlist_id):
        print(playlist_id)
        return JsonResponse({})

    def delete(self, request, playlist_id):
        print(playlist_id)
        return JsonResponse({})
