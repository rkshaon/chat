from django.urls import path

from user_api.views import v1 as v1_view


urlpatterns = [
    path(
        'registration',
        v1_view.UserRegistrationView.as_view(),
        name='user-registration',
    ),
    path(
        'login',
        v1_view.UserLoginView.as_view(),
        name='user-login',
    ),
]
