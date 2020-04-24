from django.test import Client, TestCase


class AppleMusicTokenTest(TestCase):
    """
    Test cases for Apple Music Token views
    """

    def setUp(self):
        client = Client()
        print(client)

    def test_apple_music_token_create(self):
        print("HERE FOR TEST POST")
