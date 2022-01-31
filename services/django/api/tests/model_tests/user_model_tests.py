"""
User API Test
"""
from django.test import TestCase
from api.models.core import UserProfile
from api.models.factories import UserProfileFactory


class UserTest(TestCase):
    """
    Test module for User
    """

    def test_get_single_user_simple(self):
        """
        Tests retrieving a user
        """
        UserProfileFactory(username="casperdafriendlyghost")
        casper = UserProfile.objects.get(username="casperdafriendlyghost")
        self.assertEqual(UserProfile.objects.count(), 1)
        self.assertIsInstance(casper.auth0_user_id, str)

    def test_get_multiple_users_simple(self):
        """
        Tests retrieving a user
        """
        UserProfileFactory.create_batch(25)
        self.assertEqual(UserProfile.objects.count(), 25)
