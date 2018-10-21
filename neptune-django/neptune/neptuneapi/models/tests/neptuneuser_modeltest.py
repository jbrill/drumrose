from django.test import TestCase
from .. import NeptuneUser


class PostsTest(TestCase):
    """ Test module for Puppy model """

    def setUp(self):
        NeptuneUser.objects.create(
            name='Casper', handle="casperdafriendlyghost", avatar_url="https://s.gravatar.com/avatar/5396e26cc474676468d20d3cb45cbace?s=480&r=pg&d=https%3A%2F%2Fcdn.auth0.com%2Favatars%2Fjl.png")

    def test_puppy_breed(self):
        puppy_casper = Puppy.objects.get(name='Casper')
        self.assertEqual(
            puppy_casper.get_breed(), "Casper belongs to Bull Dog breed.")
