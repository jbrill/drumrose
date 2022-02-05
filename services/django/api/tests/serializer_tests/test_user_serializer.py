"""
User Serializer Test Module
"""
from django.test import TestCase
from api.models.factories import FollowContainFactory, UserProfileFactory
from api.users.serializers import UserProfileSerializer
from api.models.core import FollowContain


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

    def test_user_serializer_with_followers(self):
        """
        Test single user serializer
        """
        user = UserProfileFactory()
        follower = UserProfileFactory()
        FollowContainFactory(following_user=user, follower_user=follower)

        # Do the serialization
        serialized_user = UserProfileSerializer(user, many=False).data

        # Assert user fields
        self.assertEqual(serialized_user["username"], str(user.username))

    def test_user_serializer_update_with_followers(self):
        """
        Test single user serializer
        """
        user = UserProfileFactory()
        follower = FollowContainFactory(following_user=user)
        # Do the serialization
        serialized_user = UserProfileSerializer(user)

        # Assert user fields
        self.assertEqual(serialized_user.data["username"], str(user.username))
        self.assertEqual(serialized_user.data["followers"], [follower.follower_user.id])
