from threading import Thread

import websocket


class RipioWebsocket(Thread):
    daemon = True

    def __init__(
        self,
        url,
        on_open=None,
        on_error=None,
        on_message=None,
        on_close=None,
        headers=None,
    ):
        self.ws_url = url
        self.on_open = on_open
        self.on_error = on_error
        self.on_message = on_message
        self.on_close = on_close
        self.headers = headers
        super().__init__()

    def run(self, *args, **kwargs):
        websocket.enableTrace(True)
        self.__websocket = websocket.WebSocketApp(
            self.ws_url,
            on_open=self.on_open,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close,
        )
        self.__websocket.run_forever()

    def send_message(self, message):
        self.__websocket.send(message)

    def close(self):
        self.__websocket.close()
