"""
User API Test
"""

from api.models.core import User
from django.test import TestCase


class UserTest(TestCase):
    """ Test module for User """

    def setUp(self):
        User.objects.create(
            name="Casper",
            handle="casperdafriendlyghost",
            avatar_url="https://i2.wp.com/cdn.auth0.com/avatars/jl.png?ssl=1",
        )

    def test_get_new_user(self):
        """
        Tests retrieving a user
        """
        casper = User.objects.get(name="Casper")
        self.assertTrue(casper.handle, "casperdafriendlyghost")
