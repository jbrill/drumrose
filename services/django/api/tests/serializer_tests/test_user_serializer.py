"""
User Serializer Test Module
"""
from django.test import TestCase
from api.models.factories import UserProfileFactory
from api.users.serializers import UserProfileSerializer


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
        user_with_followers = UserProfileFactory(followers=[user])

        # Do the serialization
        serialized_user = UserProfileSerializer(user_with_followers, many=False).data

        # Assert user fields
        self.assertEqual(serialized_user["username"], str(user_with_followers.username))

    def test_user_serializer_update_with_followers(self):
        """
        Test single user serializer
        """
        user = UserProfileFactory()
        follower = UserProfileFactory()
        new_user_data = {"followers": [follower.id]}
        # Do the serialization
        serialized_user = UserProfileSerializer(user, data=new_user_data, partial=True)
        if serialized_user.is_valid():
            serialized_user.save()
        # Assert user fields
        self.assertEqual(serialized_user.data["username"], str(user.username))
        self.assertEqual(serialized_user.data["followers"], [follower.id])
