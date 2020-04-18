"""
Post Model Test
"""

from api.models.core import Post
from api.models.factories import PostFactory, SongFactory
from django.test import TestCase


class PostTest(TestCase):
    """ Test module for Post """

    def test_get_single_post_simple(self):
        """
        Tests creating and retrieving a post
        """
        song = SongFactory()
        PostFactory(song=song, caption="test caption")

        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.first().caption, "test caption")

    def test_get_multiple_posts_simple(self):
        """
        Tests retrieving a set of posts
        """
        song = SongFactory()
        PostFactory.create_batch(50, song=song, caption="test caption")

        self.assertEqual(Post.objects.count(), 50)
        self.assertEqual(Post.objects.first().caption, "test caption")
