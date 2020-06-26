"""
Factories for api
"""
import random

import factory

from api.models.core import Album, Artist, FavoritedTrack, Song
from factory import fuzzy
from faker import Faker


fake = Faker()


class ArtistFactory(factory.DjangoModelFactory):
    class Meta:
        model = Artist

    apple_music_id = fuzzy.FuzzyInteger(1469577142, 1469597142)


class SongFactory(factory.DjangoModelFactory):
    class Meta:
        model = Song

    apple_music_id = fuzzy.FuzzyInteger(1469577142, 1469597142)


class AlbumFactory(factory.DjangoModelFactory):
    class Meta:
        model = Album

    apple_music_id = fuzzy.FuzzyInteger(1469577142, 1469597142)


class FavoritedTrackFactory(factory.DjangoModelFactory):
    class Meta:
        model = FavoritedTrack

    auth0_user_id = "auth0.5ee91b29c70eb0001935e77"
    song = factory.SubFactory("api.models.factories.SongFactory")
