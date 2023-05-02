import ripio
from ripio.examples import get_random_api_key
from ripio.trade.client import Client

mock_api_key = get_random_api_key()

# Using global api_key setting
ripio.api_key = mock_api_key


def get_wallets():
    client_handler = Client()
    return client_handler.get_wallets()


def check_wallet_internal():
    client_handler = Client()
    return client_handler.check_wallet_internal(
        "0x5c2809a8443e887ED8f8De406030D5f35F6711cb", "CREAL"
    )
