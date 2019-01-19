from django.test import TestCase, Client


class NeptunePostTest(TestCase):
    """
    Test cases for NeptunePost views
    """

    def setUp(self):
        client = Client()

    def test_post_create(self):
        print("HERE FOR TEST POST")
        pass
