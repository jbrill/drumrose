"""
Factories
"""
from factory import fuzzy
from faker import Faker
import factory
from api.models.core import (
    Album,
    AlbumReview,
    Artist,
    FavoritedAlbum,
    FavoritedPlaylist,
    FavoritedTrack,
    Playlist,
    PlaylistReview,
    Song,
    TrackReview,
    UserProfile,
)

fake = Faker()


class ArtistFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Artist

    apple_music_id = fuzzy.FuzzyInteger(1469577142, 1469597142)
    page_id = factory.Sequence(lambda n: "page %03d" % n)


class SongFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Song

    apple_music_id = fuzzy.FuzzyInteger(1469577142, 1469597142)
    name = fuzzy.FuzzyText()


class AlbumFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Album

    apple_music_id = fuzzy.FuzzyInteger(1469577142, 1469597142)
    name = fuzzy.FuzzyText()


class PlaylistFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Playlist

    apple_music_id = fuzzy.FuzzyInteger(1469577142, 1469597142)
    caption = fuzzy.FuzzyText()
    name = fuzzy.FuzzyText()

    @factory.post_generation
    def tracks(self, create, extracted):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for track in extracted:
                self.tracks.add(track)


class UserProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserProfile

    auth0_user_id = fuzzy.FuzzyInteger(1000000000, 1469597142)
    username = fuzzy.FuzzyText()
    email = factory.Faker("email")

    @factory.post_generation
    def followers(self, create, extracted):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for follower in extracted:
                self.followers.add(follower)

    @factory.post_generation
    def blocked_users(self, create, extracted):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for blocked_user in extracted:
                self.blocked_users.add(blocked_user)


class FavoritedTrackFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = FavoritedTrack

    user = factory.SubFactory("api.models.factories.UserProfileFactory")
    song = factory.SubFactory("api.models.factories.SongFactory")


class FavoritedAlbumFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = FavoritedAlbum

    user = factory.SubFactory("api.models.factories.UserProfileFactory")
    album = factory.SubFactory("api.models.factories.AlbumFactory")


class FavoritedPlaylistFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = FavoritedPlaylist

    user = factory.SubFactory("api.models.factories.UserProfileFactory")
    playlist = factory.SubFactory("api.models.factories.PlaylistFactory")


class TrackReviewFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = TrackReview

    user = factory.SubFactory("api.models.factories.UserProfileFactory")
    track = factory.SubFactory("api.models.factories.SongFactory")
    review = fuzzy.FuzzyText()
    rating = 0.5


class AlbumReviewFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = AlbumReview
        django_get_or_create = ("user", "album")

    user = factory.SubFactory("api.models.factories.UserProfileFactory")
    album = factory.SubFactory("api.models.factories.AlbumFactory")
    review = fuzzy.FuzzyText()
    rating = 0.5


class PlaylistReviewFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PlaylistReview
        django_get_or_create = ("user", "playlist")

    user = factory.SubFactory("api.models.factories.UserProfileFactory")
    playlist = factory.SubFactory("api.models.factories.PlaylistFactory")
    review = fuzzy.FuzzyText()
    rating = 0.5
