"""
Neptune User API Test
"""

from django.test import TestCase

from neptuneapi.models.neptune_core import NeptuneUser

class PostsTest(TestCase):
    """ Test module for Puppy model """

    def setUp(self):
        NeptuneUser.objects.create(
            name='Casper',
            handle="casperdafriendlyghost",
            avatar_url="https://s.gravatar.com/avatar/5396e26cc474676468d20d3cb45cbace?s=480&r=pg&d=https%3A%2F%2Fcdn.auth0.com%2Favatars%2Fjl.png"
        )

    def test_get_user(self):
        """
        Tests retrieving a user
        """
        casper = NeptuneUser.objects.get(name='Casper')
        # self.assertEqual(
        #     puppy_casper.get_breed(),
        #     "Casper belongs to Bull Dog breed."
        # )
        pass
