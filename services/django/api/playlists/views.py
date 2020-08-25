"""
Playlist Route Definition
"""
# pylint: disable=W0612,W0613

from api.models.core import FavoritedPlaylist, Playlist
from api.playlists.serializers import PlaylistSerializer
from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView


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

    def get(self, request):
        """
        Returns a list of playlists
        """
        return

    def post(self, request):
        """
        Returns a 201 if successful
        """
        return


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

    def get(self, request, playlist_id):
        """
        Returns a serialized playlist
        """
        try:
            playlist = Playlist.objects.get(id=playlist_id)
        except Playlist.DoesNotExist:
            return JsonResponse(
                {"message": "Playlist does not exist."}, status=status.HTTP_409_CONFLICT
            )
        is_favorited = FavoritedPlaylist.objects.filter(
            user=request.user, playlist=playlist
        ).exists()

        serializer = PlaylistSerializer(
            playlist, context={"is_favorited": is_favorited}
        )
        return JsonResponse({"playlist": serializer.data})

    def post(self, request):
        """
        Returns a 201 if successful
        """
        return JsonResponse({})

    def patch(self, request, playlist_id):
        print(playlist_id)
        return JsonResponse({})

    def delete(self, request, playlist_id):
        print(playlist_id)
        return JsonResponse({})
