from django.test import TestCase, Client


class PostTest(TestCase):
    """
    Test cases for Post views
    """

    def setUp(self):
        client = Client()

    def test_post_create(self):
        print("HERE FOR TEST POST")
        pass
