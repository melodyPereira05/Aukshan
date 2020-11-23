from django.urls import re_path
from . import consumers


websocket_urlpatterns = [
 re_path(r'ws/auction/(?P<item_id>\d+)/(?P<slug>[-\w]+)/$',consumers.ChatConsumer),
]