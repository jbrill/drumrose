"""
Core Models for  API
"""

import uuid

from api.services.auth0 import get_access_token, get_user
from django.contrib.auth.models import User
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


class Auth0ManagementTokenQuerySet(models.QuerySet):
    def active_token(self):
        return self.filter(is_authorized=True).last()


class Auth0ManagementTokenManager(models.Manager):
    def get_queryset(self):
        return Auth0ManagementTokenQuerySet(self.model, using=self._db)

    def active_token(self):
        active_token_queryset = self.get_queryset().active_token()
        # ensure that token exists
        if active_token_queryset:
            return active_token_queryset
        return Auth0ManagementToken.objects.create()


class Auth0ManagementToken(BaseModel):
    """
    Token for Auth0 Api Management
    """

    access_token = models.TextField(max_length=500, null=True, blank=True)
    is_authorized = models.BooleanField(default=False)

    objects = Auth0ManagementTokenManager()

    def __str__(self):
        return f"{self.access_token}"

    def save(self, *args, **kwargs):
        # lets do an call here to auth0 to check if auth works
        self.access_token = get_access_token()

        # set all tokens to not authorized
        authorized_tokens = Auth0ManagementToken.objects.all()
        authorized_tokens.update(is_authorized=False)
        self.is_authorized = True
        super(Auth0ManagementToken, self).save(*args, **kwargs)


class Artist(BaseModel):
    """
    Model for an artist
    """

    apple_music_id = models.CharField(
        max_length=200, null=True, blank=True, unique=True
    )


class Song(BaseModel):
    """
    Model for a song
    """

    apple_music_id = models.CharField(
        max_length=200, null=True, blank=True, unique=True
    )


class Album(BaseModel):
    """
    Model for an album
    """

    apple_music_id = models.CharField(
        max_length=200, null=True, blank=True, unique=True
    )


class Playlist(BaseModel):
    """
    Model for a playlist
    """

    tracks = models.ManyToManyField("Song")
    title = models.CharField(max_length=64)
    caption = models.CharField(max_length=200)
    apple_music_id = models.CharField(
        max_length=200, null=True, blank=True, unique=True
    )


class FavoritedItem(BaseModel):
    """
    Model for a favorited item
    """

    auth0_user_id = models.CharField(max_length=200)

    class Meta:
        """
        Meta Class Definition
        """

        abstract = True


class FavoritedTrack(FavoritedItem):
    """
    Model for a favorited track
    """

    song = models.ForeignKey("Song", on_delete=models.CASCADE)
    favorite_type = "track"

    class Meta:
        unique_together = (
            "auth0_user_id",
            "song",
        )


class FavoritedAlbum(FavoritedItem):
    """
    Model for a favorited album
    """

    album = models.ForeignKey("Album", on_delete=models.CASCADE)
    favorite_type = "album"

    class Meta:
        unique_together = (
            "auth0_user_id",
            "album",
        )


class FavoritedPlaylist(FavoritedItem):
    """
    Model for a favorited playlist
    """

    playlist = models.ForeignKey("Playlist", on_delete=models.CASCADE)
    favorite_type = "playlist"

    class Meta:
        unique_together = (
            "auth0_user_id",
            "playlist",
        )


class ListenedItem(BaseModel):
    """
    Model for a listened item
    """

    auth0_user_id = models.CharField(
        max_length=200, default="auth0.5ee91b29c70eb0001935e77"
    )

    class Meta:
        """
        Meta Class Definition
        """

        abstract = True


class ListenedTrack(ListenedItem):
    """
    Model for a listened track
    """

    track = models.ForeignKey("Song", on_delete=models.CASCADE)
    listened_type = "track"

    class Meta:
        unique_together = (
            "auth0_user_id",
            "track",
        )
