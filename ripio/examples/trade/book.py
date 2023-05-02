import ripio
from ripio.examples import get_random_api_key
from ripio.trade.client import Client

mock_api_key = get_random_api_key()

# Using global api_key setting
ripio.api_key = mock_api_key


def get_book_summary():
    client_handler = Client()
    return client_handler.get_book_summary("BTC_BRL")


def get_book_estimate_price():
    client_handler = Client()
    return client_handler.get_book_estimate_price(
        pair="BTC_BRL", amount="10", side="sell"
    )


def get_book_orderbook_level_3():
    client_handler = Client()
    return client_handler.get_book_orderbook_level_3(pair="BTC_BRL")


def get_book_orderbook_level_2():
    client_handler = Client()
    return client_handler.get_book_orderbook_level_2(pair="BTC_BRL")
