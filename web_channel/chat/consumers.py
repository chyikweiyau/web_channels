from datetime import datetime
from django.http import HttpResponse
from channels.handler import AsgiHandler


def http_consumer(message):
    # Make standard HTTP response - access ASGI path attribute directly
    response = HttpResponse("Success")
    # Encode that response into message format (ASGI)
    for chunk in AsgiHandler.encode_response(response):
        message.reply_channel.send(chunk)


def ws_message(message):
    # ASGI WebSocket packet-received and send-packet message types
    # both have a "text" key for their textual data.
    print message.content['text']
    ret_txt = "receive '%s' at %s".format(message.content['text'], datetime.now().isoformat())
    message.reply_channel.send({
        "text": message.content['text'],
    })
