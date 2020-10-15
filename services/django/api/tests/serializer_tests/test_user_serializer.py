"""
User Serializer Test Module
"""

from api.models.factories import UserProfileFactory
from api.users.serializers import UserProfileSerializer
from django.test import TestCase


class UserSerializerTest(TestCase):
    """
    User Serializer Test
    """

    def test_user_serializer(self):
        """
        Test single user serializer
        """
        user = UserProfileFactory()

        # Do the serialization
        serialized_user = UserProfileSerializer(user, many=False).data

        # Assert user fields
        self.assertEqual(serialized_user["username"], str(user.username))
