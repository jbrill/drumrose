"""
 User API Test
"""

from django.test import TestCase

from api.models.core import User

class PostsTest(TestCase):
    """ Test module for Post """

    def setUp(self):
        User.objects.create(
            name='Casper',
            handle="casperdafriendlyghost",
            avatar_url="https://i2.wp.com/cdn.auth0.com/avatars/jl.png?ssl=1"
        )

    def test_get_user(self):
        """
        Tests retrieving a user
        """
        casper = User.objects.get(name='Casper')
        self.assertTrue(casper.handle, "casperdafriendlyghost")
