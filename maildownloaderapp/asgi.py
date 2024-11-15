import os

import mail_app.routing
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'maildownloaderapp.settings')

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter(
    {
        'http': django_asgi_app,

        'websocket': AuthMiddlewareStack(
                URLRouter(mail_app.routing.websocket_urlpatterns)
        )
    }
)
