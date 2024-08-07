from django.urls import resolve, reverse
from django.test import TestCase
from django.test import SimpleTestCase

from user_api.models import User

from user_api.serializers import UserSerializer

from user_api.views import v1 as v1_views


class UserModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='testuser@example.com',
            username='testuser',
            password='testpassword123',
            name='Test User'
        )

    def test_user_creation(self):
        self.assertEqual(self.user.email, 'testuser@example.com')
        self.assertEqual(self.user.username, 'testuser')
        self.assertTrue(self.user.check_password('testpassword123'))
        self.assertEqual(self.user.name, 'Test User')
        self.assertTrue(self.user.is_active)
        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_superuser)

    def test_superuser_creation(self):
        superuser = User.objects.create_superuser(
            email='superuser@example.com',
            username='superuser',
            password='superpassword123'
        )
        self.assertEqual(superuser.email, 'superuser@example.com')
        self.assertEqual(superuser.username, 'superuser')
        self.assertTrue(superuser.check_password('superpassword123'))
        self.assertTrue(superuser.is_active)
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)


class UrlsTestCase(SimpleTestCase):
    def test_user_registration_url_resolves(self):
        url = reverse('user-registration')
        self.assertEqual(
            resolve(url).func.view_class,
            v1_views.UserRegistrationView,
        )

    def test_user_login_url_resolves(self):
        url = reverse('user-login')
        self.assertEqual(
            resolve(url).func.view_class,
            v1_views.UserLoginView
        )


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
