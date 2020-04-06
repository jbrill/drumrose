"""
Core Models for  API
"""

from django.db import models
from django.contrib.postgres.fields import ArrayField


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
    songs = models.ManyToManyField('Song', blank=True)
    albums = models.ManyToManyField('Album', blank=True)


class Song(BaseModel):
    """
    Model for a song
    """
    apple_music_id = models.CharField(max_length=200, unique=True)


class Album(BaseModel):
    """
    Model for an album
    """
    name = models.CharField(max_length=200)
    artwork_url = models.CharField(max_length=200)
    artists = models.ForeignKey('Artist', on_delete=models.CASCADE)
    songs = models.ManyToManyField('Song')


class User(BaseModel):
    """
    Model for a user
    """
    handle = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=200)
    avatar_url = models.CharField(max_length=200)
    posts = models.ForeignKey(
        'Post',
        blank=True,
        on_delete=models.PROTECT,
        related_name="user_posts"
    )


class Post(BaseModel):
    """
    Model for a post
    """
    song = models.ForeignKey(
        'Song',
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
        related_name="post_user"
    )
    caption = models.CharField(max_length=200)
