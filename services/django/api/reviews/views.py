"""
Reivews Route Definitions
"""

# pylint: disable=W0612,W0613
from itertools import chain
from operator import attrgetter
from django.core.serializers import serialize
from api.models.core import (
    AlbumReview,
    PlaylistReview,
    Song,
    TrackReview,
    UserProfile,
    Album,
)
from rest_framework.response import Response
from django.core import serializers

from api.reviews.serializers import (
    AlbumReviewSerializer,
    PlaylistReviewSerializer,
    TrackReviewSerializer,
)
from django.core.paginator import Paginator
from django.http import JsonResponse
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework_auth0.authentication import Auth0JSONWebTokenAuthentication
from rest_framework.renderers import JSONRenderer


class TrackReviewList(APIView):
    """
    Description:
        API View for Track Reviews List
    Routes:
        GET /reviews/tracks/
            Gets a list of track reviews
    """

    authentication_classes = [Auth0JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        """
        Get track reviews
        """
        reviews = TrackReview.objects.all()

        return JsonResponse(
            {"track_reviews": list(reviews.values())}, status=status.HTTP_200_OK
        )

    def post(self, request):
        """
        Create track review
        """
        try:
            serializer = TrackReviewSerializer(
                data={
                    "apple_music_id": request.data["apple_music_id"],
                    "name": request.data["name"],
                    "review": request.data["review"],
                },
                context={"request": request},
            )
        except KeyError:
            return JsonResponse(
                {"message": "Missing data required for serialization."},
                status=status.HTTP_422_UNPROCESSABLE_ENTITY,
            )
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(
                serializer.data, status=status.HTTP_201_CREATED, safe=False
            )
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AlbumReviewList(APIView):
    """
    Description:
        API View for Reviewed Albums
    Routes:
        GET /reviews/albums/
            Gets a list of reviewed albums
        POST /reviews/albums/
            Creates a new reviewed album
    """

    authentication_classes = [Auth0JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        """
        Get reviewed albums
        """
        reviews = AlbumReview.objects.all()

        return JsonResponse(
            {"album_reviews": list(reviews.values())}, status=status.HTTP_200_OK
        )

    def post(self, request):
        """
        Create favorited album
        """
        try:
            serializer = AlbumReviewSerializer(
                data={
                    "apple_music_id": request.data["apple_music_id"],
                    "name": request.data["name"],
                },
                context={"request": request},
            )
        except KeyError:
            return JsonResponse(
                {"message": "Missing data required for serialization."},
                status=status.HTTP_422_UNPROCESSABLE_ENTITY,
            )
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(
                serializer.data, status=status.HTTP_201_CREATED, safe=False
            )
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PlaylistReviewList(APIView):
    """
    Description:
        API View for Reviewed Playlists
    Routes:
        - GET /reviews/playlists/
            - Gets a list of reviewed playlists
        - POST /reviews/playlists/
            - Creates a new reviewed playlist
    """

    authentication_classes = [Auth0JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Get reviewed playlists
        """
        reviews = AlbumReview.objects.all()

        return JsonResponse(
            {"playlist_reviews": list(reviews.values())}, status=status.HTTP_200_OK
        )

    def post(self, request):
        """
        Post favorited playlist
        """
        try:
            serializer = PlaylistReviewSerializer(
                data={
                    "apple_music_id": request.data["apple_music_id"],
                    "name": request.data["name"],
                },
                context={"request": request},
            )
        except KeyError:
            return JsonResponse(
                {"message": "Missing data required for serialization."},
                status=status.HTTP_422_UNPROCESSABLE_ENTITY,
            )
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(
                serializer.data, status=status.HTTP_201_CREATED, safe=False
            )
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
