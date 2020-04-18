"""
User API Test
"""

from api.models.core import User
from api.models.factories import UserFactory
from django.test import TestCase


class UserTest(TestCase):
    """ Test module for User """

    def test_get_single_user_simple(self):
        """
        Tests retrieving a user
        """
        UserFactory(name="Casper", handle="casperdafriendlyghost")
        casper = User.objects.get(name="Casper")
        self.assertEqual(casper.handle, "casperdafriendlyghost")

    def test_get_multiple_users_simple(self):
        """
        Tests retrieving a user
        """
        UserFactory(name="Casper", handle="casperdafriendlyghost")
        casper = User.objects.get(name="Casper")
        self.assertEqual(casper.handle, "casperdafriendlyghost")

        UserFactory.create_batch(25)
        self.assertEqual(User.objects.count(), 26)
