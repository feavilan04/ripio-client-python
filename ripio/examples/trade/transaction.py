import ripio
from ripio.examples import get_random_api_key
from ripio.trade.client import Client

mock_api_key = get_random_api_key()

# Using global api_key setting
ripio.api_key = mock_api_key


def synchronize_transaction():
    client_handler = Client()
    return client_handler.synchronize_transaction(
        "7b6155e3d010b530f484e0cd05429328a514dd0158dc31c23cdd3ebb59f335ae",
        "ETH",
    )
