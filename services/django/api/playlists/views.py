"""
Playlist Route Definition
"""
# pylint: disable=W0612,W0613

from api.models.core import Playlist
from api.playlists.serializers import PlaylistSerializer
from rest_framework.response import Response
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
        playlists = Playlist.objects.all()

        serializer = PlaylistSerializer(playlists, many=True)
        return Response(serializer.data)

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
        pass

    def patch(self, request, playlist_id):
        pass

    def delete(self, request, playlist_id):
        pass
