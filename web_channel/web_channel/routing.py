from channels.routing import route
from chat.consumers import ws_message


channel_routing = [
    route("http.request", "chat.consumers.http_consumer", path=r'^health_check/'),
    route("websocket.receive", ws_message),
]
