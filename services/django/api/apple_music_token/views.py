"""
Apple-Music-Token Route Definition
"""
# pylint: disable=W0612,W0613
from rest_framework.response import Response
from rest_framework.views import APIView
from api.settings import APPLE_MUSIC_TOKEN_GENERATOR


class AppleMusicTokenRoute(APIView):
    """
    Description:
        - API View for Apple Music Token
    Routes:
        - POST /apple-music-token/
            - Generates a new apple music token
    """

    authentication_classes = []
    permission_classes = []

    def post(self, request):
        """
        Generate Apple Music Token
        """
        token = APPLE_MUSIC_TOKEN_GENERATOR.generate_token()
        return Response({"token": token})
