"""
ASGI config for realtime_chat project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

# import django
# from channels.http import AsgiHandler
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from chatapp.routing import websocket_urlpatterns
# import chatapp.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'realtime_chat.settings')

application = ProtocolTypeRouter({
    # 'http': AsgiHandler(),
    "http": get_asgi_application(),
    # Just HTTP for now. (We can add other protocols later.)
    "websocket": AuthMiddlewareStack(
        URLRouter(
            # chat.routing.websocket_urlpatterns
            # chatapp.routing.websocket_urlpatterns
            websocket_urlpatterns
        )
    ),
})
# application = get_asgi_application()
