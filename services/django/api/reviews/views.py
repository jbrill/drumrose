"""
Reivews Route Definitions
"""
# pylint: disable=W0612,W0613
import json
from itertools import chain
from operator import attrgetter

from api.models.core import (
    AlbumReview,
    PlaylistReview,
    Review,
    TrackReview,
    UserProfile,
)
from api.reviews.serializers import (
    AlbumReviewSerializer,
    PlaylistReviewSerializer,
    ReviewSerializer,
    TrackReviewSerializer,
)
from api.users.serializers import UserProfileSerializer
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_auth0.authentication import Auth0JSONWebTokenAuthentication


class TrackReviewList(APIView):
    """
    Description:
        API View for Track Reviews List
    Routes:
        GET /reviews/tracks/
            Gets a list of track reviews
    """

    authentication_classes = []
    permission_classes = []

    def get(self, request):
        """
        Get track reviews
        """
        reviews = TrackReview.objects.all()

        serializer = TrackReviewSerializer(reviews, many=True)
        return JsonResponse({"track_reviews": serializer.data})

    def post(self, request):
        """
        Create track review
        """
        print(request.data)
        try:
            serializer = TrackReviewSerializer(
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

    authentication_classes = []
    permission_classes = []

    def get(self, request):
        """
        Get reviewed albums
        """
        reviewed_albums = AlbumReview.objects.all()

        serializer = AlbumReviewSerializer(reviewed_albums, many=True)
        return JsonResponse({"album_reviews": serializer.data})

    def post(self, request):
        """
        Create favorited album
        """
        return


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
        reviewed_playlists = PlaylistReview.objects.all()

        serializer = PlaylistReviewSerializer(reviewed_playlists, many=True)
        return JsonResponse({"playlist_reviews": serializer.data})

    def post(self, request):
        """
        Post favorited playlist
        """

        return


class ReviewsList(APIView):
    """
    Description:
        API View for Reviews
    Routes:
        GET /reviews/
            Gets a list of followers' favorites
    """

    authentication_classes = []
    permission_classes = []

    def get(self, request):
        """
        Get favorites from followers
        """
        reviewed_playlists = PlaylistReview.objects.all()
        reviewed_tracks = TrackReview.objects.all()
        reviewed_albums = AlbumReview.objects.all()

        # merge favorites
        sorted_reviews = sorted(
            chain(reviewed_playlists, reviewed_tracks, reviewed_albums),
            key=attrgetter("created_date"),
            reverse=True,
        )
        query = Paginator(sorted_reviews, 10)
        page = query.page(1)
        reviews = page.object_list
        serializer = ReviewSerializer(reviews, many=True)
        return JsonResponse(serializer.data, safe=False)


class RecentReviewsList(APIView):
    """
    Description:
        API View for Recent Reviews
    Routes:
        GET /reviews/recent/
            Gets a list of recent reviews
    """

    authentication_classes = []
    permission_classes = []

    def get(self, request):
        """
        Get recent reviews
        """
        reviewed_playlists = PlaylistReview.objects.all()
        reviewed_tracks = TrackReview.objects.all()
        reviewed_albums = AlbumReview.objects.all()

        # merge favorites
        sorted_reviews = sorted(
            chain(reviewed_playlists, reviewed_tracks, reviewed_albums),
            key=attrgetter("created_date"),
            reverse=True,
        )
        query = Paginator(sorted_reviews, 10)
        page = query.page(1)
        reviews = page.object_list
        serializer = ReviewSerializer(reviews, many=True)
        return JsonResponse(serializer.data, safe=False)
