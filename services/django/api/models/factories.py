"""
Factories for api
"""
import random

import factory

from faker import Faker
from factory import fuzzy
from api.models.core import (
    Song,
    Album,
    Artist,
    Playlist,
    UserProfile,
    FavoritedAlbum,
    FavoritedTrack,
    FavoritedPlaylist,
)


fake = Faker()


class ArtistFactory(factory.DjangoModelFactory):
    class Meta:
        model = Artist

    apple_music_id = fuzzy.FuzzyInteger(1469577142, 1469597142)
    page_id = factory.Sequence(lambda n: "page %03d" % n)


class SongFactory(factory.DjangoModelFactory):
    class Meta:
        model = Song

    apple_music_id = fuzzy.FuzzyInteger(1469577142, 1469597142)
    page_id = factory.Sequence(lambda n: "page %03d" % n)


class AlbumFactory(factory.DjangoModelFactory):
    class Meta:
        model = Album

    apple_music_id = fuzzy.FuzzyInteger(1469577142, 1469597142)
    page_id = factory.Sequence(lambda n: "page %03d" % n)


class PlaylistFactory(factory.DjangoModelFactory):
    class Meta:
        model = Playlist

    apple_music_id = fuzzy.FuzzyInteger(1469577142, 1469597142)
    caption = fuzzy.FuzzyText()
    page_id = factory.Sequence(lambda n: "page %03d" % n)
    title = fuzzy.FuzzyText()

    @factory.post_generation
    def tracks(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for track in extracted:
                self.tracks.add(track)


class UserProfileFactory(factory.DjangoModelFactory):
    class Meta:
        model = UserProfile

    auth0_user_id = fuzzy.FuzzyInteger(1469577142, 1469597142)
    username = factory.Sequence(lambda n: "Agent %03d" % n)
    email = factory.Sequence(lambda n: "person{}@example.com".format(n))

    @factory.post_generation
    def followers(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for follower in extracted:
                self.followers.add(follower)

    @factory.post_generation
    def blocked_users(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for blocked_user in extracted:
                self.blocked_users.add(blocked_user)


class FavoritedTrackFactory(factory.DjangoModelFactory):
    class Meta:
        model = FavoritedTrack

    user = factory.SubFactory("api.models.factories.UserProfileFactory")
    song = factory.SubFactory("api.models.factories.SongFactory")


class FavoritedAlbumFactory(factory.DjangoModelFactory):
    class Meta:
        model = FavoritedAlbum

    user = factory.SubFactory("api.models.factories.UserProfileFactory")
    album = factory.SubFactory("api.models.factories.AlbumFactory")


class FavoritedPlaylistFactory(factory.DjangoModelFactory):
    class Meta:
        model = FavoritedPlaylist

    user = factory.SubFactory("api.models.factories.UserProfileFactory")
    playlist = factory.SubFactory("api.models.factories.Playlist")
