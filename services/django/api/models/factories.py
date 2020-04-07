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
    name = fake.name()

    @factory.post_generation
    def posts(self, create, extracted):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for post in extracted:
                self.posts.add(post)


class ArtistFactory(factory.DjangoModelFactory):
    class Meta:
        model = Artist

    name = fake.name()


class SongFactory(factory.DjangoModelFactory):
    class Meta:
        model = Song

    name = fake.name()

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

    name = fake.name()

    @factory.post_generation
    def artists(self, create, extracted):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for artist in extracted:
                self.artists.add(artist)


class PostFactory(factory.DjangoModelFactory):
    class Meta:
        model = Post

    song = factory.SubFactory("api.models.factories.SongFactory")
    caption = fake.text()
