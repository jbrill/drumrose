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
    apple_music_id = models.CharField(
        max_length=200, null=True, blank=True, unique=True
    )


class Album(BaseModel):
    """
    Model for an album
    """

    name = models.CharField(max_length=200)
    artwork_url = models.CharField(max_length=200)
    apple_music_id = models.CharField(
        max_length=200, null=True, blank=True, unique=True
    )


class User(BaseModel):
    """
    Model for a user
    """

    handle = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=200)
    avatar_url = models.CharField(max_length=200)


class Playlist(BaseModel):
    """
    Model for a playlist
    """

    tracks = models.ManyToManyField("Song")
    title = models.CharField(max_length=64)
    caption = models.CharField(max_length=200)
    user = models.ForeignKey(
        "User", null=True, blank=True, on_delete=models.CASCADE
    )
    apple_music_id = models.CharField(
        max_length=200, null=True, blank=True, unique=True
    )


class FavoritedItem(BaseModel):
    """
    Model for a favorited track
    """

    user = models.ForeignKey(
        "User", null=True, blank=True, on_delete=models.CASCADE
    )

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
            "user",
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
            "user",
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
            "user",
            "playlist",
        )
