"""
API Tests for User Views
"""
import json

from api.models.core import UserProfile
from api.models.factories import UserProfileFactory
from api.tests.api_tests.util import get_test_token
from api.users.serializers import UserProfileSerializer
from api.users.views import UserDetail, UserList
from django.test import RequestFactory, TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate

factory = APIRequestFactory()


class UserListTest(TestCase):
    """
    Test cases for user list
    """

    def setUp(self):
        """
        Creates models on setup
        """
        self.token = json.loads(get_test_token())["access_token"]
        test_username = "test_username"
        test_auth0_user_id = "ApqgC9UHWyDV0Qb6rv3cby0gP47u5ZmO@clients"

        self.user = UserProfileFactory.create(
            auth0_user_id=test_auth0_user_id, username=test_username
        )

    def test_get_all_users(self):
        view = UserList.as_view()
        request = factory.get(
            reverse("UserList"),
            content_type="application/json",
            data={},
            HTTP_AUTHORIZATION="Bearer " + self.token,
        )
        response = view(request)
        print(response)
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
        view = UserList.as_view()
        request = factory.post(
            reverse("UserList"),
            content_type="application/json",
            data={
                "email": self.user.email,
                "username": "test_username_2",
                "id": "test_auth0_user_id",
            },
            HTTP_AUTHORIZATION="Bearer " + self.token,
        )
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        request = factory.post(
            reverse("UserList"),
            content_type="application/json",
            data={
                "email": "unique_email",
                "username": self.user.username,
                "id": "test_auth0_user_id",
            },
            HTTP_AUTHORIZATION="Bearer " + self.token,
        )
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        request = factory.post(
            reverse("UserList"),
            content_type="application/json",
            data={
                "email": "unique_email",
                "username": "unique_username",
                "id": self.user.auth0_user_id,
            },
            HTTP_AUTHORIZATION="Bearer " + self.token,
        )
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user(self):
        """
        Create a user
        """
        view = UserList.as_view()

        request = factory.post(
            reverse("UserList"),
            content_type="application/json",
            data={
                "email": "unique_email@email.com",
                "username": "test_username_2",
                "id": "12345",
            },
            HTTP_AUTHORIZATION="Bearer " + self.token,
        )
        response = view(request)
        print(response)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_user_missing_field(self):
        """
        Attempt to create a user with missing request data
        """
        view = UserList.as_view()

        # missing 'id'
        request = factory.post(
            reverse("UserList"),
            content_type="application/json",
            data={
                "email": self.user.email,
                "username": "test_username_2",
                "id": "test",
            },
            HTTP_AUTHORIZATION="Bearer " + self.token,
        )
        response = view(request)
        print(response)
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)

        # missing 'username'
        request = factory.post(
            reverse("UserList"),
            content_type="application/json",
            data={"email": "unique_email", "id": "test_auth0_user_id"},
            HTTP_AUTHORIZATION="Bearer " + self.token,
        )
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)

        # missing 'email'
        request = factory.post(
            reverse("UserList"),
            content_type="application/json",
            data={"email": "unique_email", "username": "unique_username"},
            HTTP_AUTHORIZATION="Bearer " + self.token,
        )
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)
