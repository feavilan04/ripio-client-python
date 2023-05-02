from ripio.core import RipioClient


class Client(RipioClient):
    def __init__(self, wallet_private_key, client_id=None, client_secret=None):
        super().__init__(wallet_private_key, client_id, client_secret)
