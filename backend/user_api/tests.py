from django.test import TestCase
from user_api.models import User


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
