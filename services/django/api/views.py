"""
Views Route Definition
"""
# pylint: disable=W0612,W0613

from django.http import JsonResponse
from rest_framework.views import APIView


class HealthRoute(APIView):
    """
    Description:
        - API View for Health Check
    Routes:
        - GET /
            - Basic response
    """

    permission_classes = []
    authentication_classes = []

    def get(self, request):
        """
        Basic GET
        """
        return JsonResponse({"status": "ok"})
