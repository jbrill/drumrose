"""
 Post Route Definition
"""

import json

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.http import HttpResponseBadRequest

from api.models.core import (
    User, Post, Song
)
from api.posts.serializers import PostSerializer


class PostList(APIView):
    """
    Description:
        - API View for User List
    Routes:
        - GET /posts/
            - Gets a list of posts per user
        - POST /posts/
            - Creates a new post
    """

    def get(self, request):
        """
        If 'feed'
          # Grab followers
            # Grab most recent posts
        If 'discover'
          # Grab recommended
        """
        posts = Post.objects.all()

        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Requires:
            - Handle
            - Apple Music Id
            - Caption
        """
        request_body = json.loads(request.body.decode('utf-8'))

        apple_music_id = request_body["apple_music_id"]
        caption = request_body["caption"]
        user_handle = request_body["handle"]
        # create new song if one doesnt exist
        try:
            song = Song.objects.get(
                apple_music_id=apple_music_id
            )
        except Song.DoesNotExist:
            song = Song.objects.create(
                apple_music_id=apple_music_id,
            )
        try:
            user = User.objects.get(
                handle=user_handle
            )
        except User.DoesNotExist:
            return HttpResponseBadRequest(
                content='{} does not exist.'.format(user_handle)
            )

        new_post = Post.objects.create(
            song=song,
            caption=caption,
            user=user
        )

        serializer = PostSerializer(new_post)
        return Response(serializer.data)


class PostDetail(APIView):
    """
    Description:
        - API View for Post Detail
    Routes:
        - GET /posts/:post_id
            - Gets a post
        - PATCH /posts/:post_id
            - Updates a post
        - DELETE /posts/:post_id
            - Deletes a post
    """

    def get(self, request, post_id):
        print("HERE...")
        user = User.objects.get(
            handle=user_handle
        )

        serializer = UserSerializer(user)
        return Response(serializer.data)

    def patch(self, request, post_id):
        post = User.objects.get(
            handle=post_id
        )

        # Update user shit

        serializer = UserSerializer(post)
        return Response(serializer.data)

    def delete(self, request, post_id):
        post = User.objects.get(
            handle=post_id
        ).delete()

        serializer = UserSerializer(post)
        return Response(serializer.data)