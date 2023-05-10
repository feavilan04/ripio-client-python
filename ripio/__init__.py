from enum import Enum, EnumMeta

from ripio.b2b.client import Client as B2BClient
from ripio.exceptions.request import InvalidNetwork
from ripio.trade.client import Client as TradeClient

BASE_URL = "http://localhost:9200/"


class MetaEnum(EnumMeta):
    def __contains__(cls, item):
        try:
            cls(item)
        except ValueError:
            return False
        return True

    def __str__(cls):
        values = "', '".join([item.value for item in cls])
        return f"'{values}'"


class BaseEnum(Enum, metaclass=MetaEnum):
    pass


class NetworksEnum(BaseEnum):
    Ethereum = "ethereum"
    Lachain = "lachain"
    Polygon = "polygon"


class Client(object):
    def __init__(
        self,
        private_key,
        network=NetworksEnum.Ethereum.value,
        api_key=None,
        client_id=None,
        client_secret=None,
    ):
        if network not in NetworksEnum:
            raise InvalidNetwork(f"'{network}' is not a supported network")
        self.trade = TradeClient(private_key, network, api_key)
        self.b2b = B2BClient(private_key, network, client_id, client_secret)
