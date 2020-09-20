from django.test import Client, TestCase


class PostTest(TestCase):
    """
    Test cases for Post views
    """

    def setUp(self):
        client = Client()
        print(client)

    def test_post_create(self):
        print("HERE FOR TEST POST")
