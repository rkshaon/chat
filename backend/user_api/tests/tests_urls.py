from django.test import SimpleTestCase
from django.urls import resolve, reverse

from user_api.views import v1 as v1_views


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
