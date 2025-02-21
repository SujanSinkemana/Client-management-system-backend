from django.urls import re_path,path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<conversation_id>\w+)/$', consumers.SecureChatConsumer.as_asgi()),
    # path('ws/chat/<str:room_name>/', consumers.SecureChatConsumer.as_asgi()),
    # path('ws/chat/', consumers.SecureChatConsumer.as_asgi()),
]