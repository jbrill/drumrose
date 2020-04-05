"""
Core Models for Neptune API
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


class NeptuneArtist(BaseModel):
    """
    Model for an artist
    """
    name = models.CharField(max_length=200)
    songs = models.ManyToManyField('NeptuneSong', blank=True)
    albums = models.ManyToManyField('NeptuneAlbum', blank=True)


class NeptuneSong(BaseModel):
    """
    Model for a song
    """
    apple_music_id = models.CharField(max_length=200, unique=True)


class NeptuneAlbum(BaseModel):
    """
    Model for an album
    """
    name = models.CharField(max_length=200)
    artwork_url = models.CharField(max_length=200)
    artist = models.ForeignKey('NeptuneArtist', on_delete=models.CASCADE)
    songs = models.ManyToManyField('NeptuneSong')


class NeptuneUser(BaseModel):
    """
    Model for a user
    """
    handle = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=200)
    avatar_url = models.CharField(max_length=200)
    posts = models.ForeignKey(
        'NeptunePost', blank=True, null=True, on_delete=models.CASCADE
    )


class NeptunePost(BaseModel):
    """
    Model for a post
    """
    song = models.ForeignKey(
        NeptuneSong,
        on_delete=models.CASCADE,
    )
    caption = models.CharField(max_length=200)
    user = models.ForeignKey('NeptuneUser', on_delete=models.CASCADE)
