import ripio
from ripio.examples import get_random_api_key
from ripio.trade.client import Client

mock_api_key = get_random_api_key()

# Using global api_key setting
ripio.api_key = mock_api_key


def get_witdrawals():
    client_handler = Client()
    return client_handler.get_witdrawals("BTC", "pending")


def get_withdrawal_estimate_fee():
    client_handler = Client()
    return client_handler.get_withdrawal_estimate_fee("BTC", "bitcoin_testnet")


def create_witdrawal():
    client_handler = Client()
    return client_handler.create_witdrawal(
        "fast",
        0.001,
        "1AU4BoYaxSunkEWikEMYXJ41c9bvQG6Wa2",
        "bitcoin",
        "bitcoin_testnet",
    )
