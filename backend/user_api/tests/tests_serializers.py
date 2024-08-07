from django.test import TestCase

from user_api.models import User

from user_api.serializers import UserSerializer


class UserSerializerTestCase(TestCase):
    def setUp(self):
        self.user_attributes = {
            'email': 'testuser1@example.com',
            'username': 'testuser1',
            'name': 'Test User1',
            'password': 'testpassword123'
        }
        self.serializer_data = {
            'email': 'testuser2@example.com',
            'username': 'testuser2',
            'name': 'Test User2',
            'password': 'testpassword123'
        }
        self.user = User.objects.create(**self.user_attributes)
        self.serializer = UserSerializer(instance=self.user)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(
            ['id', 'email', 'name', 'username']))

    def test_email_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['email'], self.user_attributes['email'])

    def test_create_user(self):
        serializer = UserSerializer(data=self.serializer_data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        user = serializer.save()
        self.assertEqual(user.email, self.serializer_data['email'])
        self.assertEqual(user.username, self.serializer_data['username'])
        self.assertEqual(user.name, self.serializer_data['name'])
        self.assertTrue(user.check_password(self.serializer_data['password']))
