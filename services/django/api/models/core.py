"""
Core Models for  API
"""

import uuid

from django.db import models


class BaseModel(models.Model):
    """
    Base model
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Meta Class Definition
        """

        abstract = True


class Artist(BaseModel):
    """
    Model for an artist
    """

    name = models.CharField(max_length=200)
    artist_photo_url = models.CharField(max_length=200, null=True)


class Song(BaseModel):
    """
    Model for a song
    """

    name = models.CharField(max_length=200)
    album = models.ForeignKey(
        "Album", null=True, blank=True, on_delete=models.CASCADE,
    )
    artist = models.ForeignKey(
        "Artist", null=True, blank=True, on_delete=models.CASCADE,
    )
    apple_music_id = models.CharField(max_length=200, null=True, blank=True)


class Album(BaseModel):
    """
    Model for an album
    """

    name = models.CharField(max_length=200)
    artwork_url = models.CharField(max_length=200)


class User(BaseModel):
    """
    Model for a user
    """

    handle = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=200)
    avatar_url = models.CharField(max_length=200)


class Post(BaseModel):
    """
    Model for a post
    """

    song = models.ForeignKey("Song", on_delete=models.CASCADE)
    caption = models.CharField(max_length=200)
    user = models.ForeignKey(
        "User", null=True, blank=True, on_delete=models.CASCADE
    )
