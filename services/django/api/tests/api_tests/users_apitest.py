"""
API Tests for User Views
"""
import json

from api.models.core import UserProfile
from api.models.factories import UserProfileFactory
from api.tests.api_tests.util import ACCESS_TOKEN, get_test_token
from api.users.serializers import UserProfileSerializer
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient


class UserListTest(TestCase):
    """
    Test cases for user list
    """

    def setUp(self):
        """
        Creates models on setup
        """
        self.token = get_test_token()
        # self.token = ACCESS_TOKEN
        self.client = APIClient()

        test_username = "test_username"
        test_auth0_user_id = "ApqgC9UHWyDV0Qb6rv3cby0gP47u5ZmO@clients"

        self.user = UserProfileFactory.create(
            auth0_user_id=test_auth0_user_id, username=test_username
        )

    def test_get_all_users(self):
        response = self.client.get(
            reverse("UserList"),
            content_type="application/json",
            data={},
            HTTP_AUTHORIZATION="Bearer " + self.token,
        )

        user_list_response = json.loads(response.content)
        user = UserProfile.objects.get(id=self.user.id)
        serializer = UserProfileSerializer(user)
        self.assertEqual(
            user_list_response["users"][0]["username"], serializer.data.get("username")
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_invalid_user_already_exists(self):
        """
        Attempt to create a user that with an fields that already exist
        """
        response = self.client.post(
            reverse("UserList"),
            content_type="application/json",
            data={
                "email": self.user.email,
                "username": "test_username_2",
                "id": "test_auth0_user_id",
            },
            HTTP_AUTHORIZATION="Bearer " + self.token,
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        response = self.client.post(
            reverse("UserList"),
            content_type="application/json",
            data={
                "email": "unique_email",
                "username": self.user.username,
                "id": "test_auth0_user_id",
            },
            HTTP_AUTHORIZATION="Bearer " + self.token,
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        response = self.client.post(
            reverse("UserList"),
            content_type="application/json",
            data={
                "email": "unique_email",
                "username": "unique_username",
                "id": self.user.auth0_user_id,
            },
            HTTP_AUTHORIZATION="Bearer " + self.token,
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user(self):
        """
        Create a user
        """
        response = self.client.post(
            reverse("UserList"),
            content_type="application/json",
            data=json.dumps(
                {
                    "email": "unique_email@email.com",
                    "username": "test_username_2",
                    "id": "12345",
                }
            ),
            HTTP_AUTHORIZATION="Bearer " + self.token,
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_user_missing_field(self):
        """
        Attempt to create a user with missing request data
        """
        # missing 'id'
        response = self.client.post(
            reverse("UserList"),
            content_type="application/json",
            data=json.dumps(
                {"email": "unique_email_2@gmail.com", "username": "test_username_2"}
            ),
            HTTP_AUTHORIZATION="Bearer " + self.token,
        )
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)

        # missing 'username'
        response = self.client.post(
            reverse("UserList"),
            content_type="application/json",
            data=json.dumps(
                {"email": "unique_email_2@gmail.com", "id": "test_auth0_user_id"}
            ),
            HTTP_AUTHORIZATION="Bearer " + self.token,
        )
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)

        response = self.client.post(
            reverse("UserList"),
            content_type="application/json",
            data=json.dumps(
                {
                    "email": "unique_email_2@gmail.com",
                    "username": "unique_username",
                    "id": "test_auth0_user_id",
                }
            ),
            HTTP_AUTHORIZATION="Bearer " + self.token,
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
