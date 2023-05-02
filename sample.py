import time

import ripio
from ripio.trade.websocket import RipioTradeWebsocket

ripio.api_key = (
    "U2FsdGVkX1+XtVrDRsxsAkMgY9zUpuLHDDVFegsTfAk8gzfLG99IYram7yVkcfIU"
)


def message_callback(*args, **kwargs):
    print("Message Arguments", args)
    print("Message Kwargs", kwargs)
    # ws_connection.close()


def error_callback(*args, **kwargs):
    print("Error Arguments", args)
    print("Error Kwargs", kwargs)


def close_callback(*args, **kwargs):
    print("Close Arguments", args)
    print("Close Kwargs", kwargs)


def open_callback(*args, **kwargs):
    print("Open Arguments", args)
    print("Open Kwargs", kwargs)
    ws_connection.send_message({"sample": "data"})


ws_connection = RipioTradeWebsocket(
    on_open=open_callback,
    on_message=message_callback,
    on_close=close_callback,
    on_error=error_callback,
)

while True:
    print("running")
    time.sleep(3)
    ws_connection.send_message({"method": "PING", "topics": "hello"})
    print("this will never be executed")
