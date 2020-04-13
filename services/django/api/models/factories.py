"""
Factories for api
"""
import factory

from api.models.core import Album, Artist, Post, Song, User
from faker import Faker


fake = Faker()


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = User

    handle = factory.Sequence(lambda n: "john%s" % n)
    name = factory.LazyAttribute(lambda _: fake.name())
    avatar_url = "test_url"


class ArtistFactory(factory.DjangoModelFactory):
    class Meta:
        model = Artist

    name = factory.LazyAttribute(lambda _: fake.name())


class SongFactory(factory.DjangoModelFactory):
    class Meta:
        model = Song

    name = factory.LazyAttribute(lambda _: fake.name())
    album = factory.SubFactory("api.models.factories.AlbumFactory")

    @factory.post_generation
    def artists(self, create, extracted):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for artist in extracted:
                self.artists.add(artist)

    @factory.post_generation
    def albums(self, create, extracted):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for album in extracted:
                self.albums.add(album)


class AlbumFactory(factory.DjangoModelFactory):
    class Meta:
        model = Album

    name = factory.LazyAttribute(lambda _: fake.name())
    artwork_url = "test_url"


class PostFactory(factory.DjangoModelFactory):
    class Meta:
        model = Post

    song = factory.SubFactory("api.models.factories.SongFactory")
    caption = factory.LazyAttribute(lambda _: fake.text())
    user = factory.SubFactory("api.models.factories.UserFactory")
