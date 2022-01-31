"""
Auth Module
"""
from rest_framework.views import APIView


class AuthRoute(APIView):
    """
    Auth Route View
    """

    def get(self, request):
        """
        Auth Module GET
        """
        print(request)

    def post(self, request):
        """
        Auth Module POST
        """
        print(request)
