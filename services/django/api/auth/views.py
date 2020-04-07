"""
Auth Module
"""

from rest_framework.views import APIView


class AuthRoute(APIView):
    def get(self, request):
        print(request)

    def post(self, request):
        print(request)
