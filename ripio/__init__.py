from ripio.b2b.client import Client as B2BClient
from ripio.trade.client import Client as TradeClient


class Client(object):
    def __init__(
        self, private_key, api_key=None, client_id=None, client_secret=None
    ):
        self.trade = TradeClient(private_key, api_key)
        self.b2b = B2BClient(private_key, client_id, client_secret)
