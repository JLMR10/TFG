from django.urls import re_path
from tfgApp import views
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator
from tfgApp.consumer import ChatConsumer

application = ProtocolTypeRouter({
    # Empty for now (http->django views is added by default)
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                [
                    re_path(r'demoChat/(?P<gameId>.*)$', ChatConsumer),
                ]
            )
        )
    )
})