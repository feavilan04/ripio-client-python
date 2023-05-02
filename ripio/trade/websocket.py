import json

import ripio
from ripio.websocket import RipioWebsocket


class RipioTradeWebsocket:
    SUBSCRIBE = "subscribe"
    UNSUBSCRIBE = "unsubscribe"
    PING = "ping"

    WS_URL = ripio.RIPIO_TRADE_WS_URL

    def __init__(
        self, on_open=None, on_error=None, on_message=None, on_close=None
    ):
        self.ws_handler = RipioWebsocket(
            self.WS_URL, on_open, on_error, on_message, on_close
        )
        self.ws_handler.start()

    def send_message(self, body):
        if "method" not in body or "topics" not in body:
            raise Exception("Message body is not well formatted")

        if body.get("method") not in (
            self.SUBSCRIBE,
            self.UNSUBSCRIBE,
            self.PING,
        ):
            raise Exception("'method' is not supported")

        if not isinstance(body.get("topics"), list):
            raise Exception("'topics' is not well formatted")

        json_body = json.dumps(body)
        self.ws_handler.send_message(json_body)

    def close(self):
        self.ws_handler.close()
