from django.db import models

class NeptuneArtist(models.Model):
    name = models.CharField(max_length=200)

class NeptuneSong(models.Model):
    name = models.CharField(max_length=200)

class NeptuneAlbum(models.Model):
    name = models.CharField(max_length=200)
    artwork_url = models.CharField(max_length=200)

class NeptuneUser(models.Model):
    """
    Model for a user
    """
    name = models.CharField(max_length=200)
    handle = models.CharField(max_length=200)
    avatar_url = models.CharField(max_length=200)

class NeptunePost(models.Model):
    song = models.ForeignKey(
        NeptuneSong,
        on_delete=models.CASCADE,
    )
    caption = models.CharField(max_length=200)

