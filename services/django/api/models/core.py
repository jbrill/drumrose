"""
Core Models for  API
"""

from django.db import models


class BaseModel(models.Model):
    """
    Base model
    """

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


class Song(BaseModel):
    """
    Model for a song
    """

    name = models.CharField(max_length=200)
    albums = models.ManyToManyField(
        "Album", related_name="songs", related_query_name="song"
    )
    artists = models.ManyToManyField(
        "Artist", related_name="songs", related_query_name="song"
    )


class Album(BaseModel):
    """
    Model for an album
    """

    name = models.CharField(max_length=200)
    artwork_url = models.CharField(max_length=200)
    artists = models.ManyToManyField(
        "Artist", related_name="albums", related_query_name="album"
    )


class User(BaseModel):
    """
    Model for a user
    """

    handle = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=200)
    avatar_url = models.CharField(max_length=200)
    posts = models.ManyToManyField(
        "Post", related_name="users", related_query_name="user"
    )


class Post(BaseModel):
    """
    Model for a post
    """

    song = models.ForeignKey("Song", on_delete=models.CASCADE)
    caption = models.CharField(max_length=200)
