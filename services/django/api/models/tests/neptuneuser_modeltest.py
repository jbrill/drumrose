"""
 User API Test
"""

from django.test import TestCase

from api.models.core import User

class PostsTest(TestCase):
    """ Test module for Puppy model """

    def setUp(self):
        User.objects.create(
            name='Casper',
            handle="casperdafriendlyghost",
            avatar_url="https://s.gravatar.com/avatar/5396e26cc474676468d20d3cb45cbace?s=480&r=pg&d=https%3A%2F%2Fcdn.auth0.com%2Favatars%2Fjl.png"
        )

    def test_get_user(self):
        """
        Tests retrieving a user
        """
        casper = User.objects.get(name='Casper')
        # self.assertEqual(
        #     puppy_casper.get_breed(),
        #     "Casper belongs to Bull Dog breed."
        # )
        pass
