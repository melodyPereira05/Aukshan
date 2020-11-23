from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import auctionItem.routing


application = ProtocolTypeRouter({
 
 'websocket': AuthMiddlewareStack(
     
    URLRouter(
    auctionItem.routing.websocket_urlpatterns
    )
 ),
})