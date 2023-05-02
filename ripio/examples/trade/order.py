import ripio
from ripio.examples import get_random_api_key
from ripio.trade.client import Client

mock_api_key = get_random_api_key()

# Using global api_key setting
ripio.api_key = mock_api_key


def get_orders():
    client_handler = Client()
    return client_handler.get_orders("ETH_BRL")


def create_order():
    client_handler = Client()
    return client_handler.create_order(
        pair="ETH_BRL", side="sell", type="market", value=10
    )


def cancel_order():
    client_handler = Client()
    return client_handler.cancel_order("02601618-18C2-4227-8437-EE2CBAC5D40C")


def get_open_orders():
    client_handler = Client()
    return client_handler.get_open_orders(pair="ETH_BRL", side="buy")


def get_order_by_id():
    client_handler = Client()
    return client_handler.get_order_by_id(
        "02601618-18C2-4227-8437-EE2CBAC5D40C"
    )


def get_order_by_external_id():
    client_handler = Client()
    return client_handler.get_order_by_external_id(
        "7269b78b-8a92-4632-be91-6f786a96e3aa"
    )


def cancel_order_by_external_id():
    client_handler = Client()
    return client_handler.cancel_order_by_external_id(
        "7269b78b-8a92-4632-be91-6f786a96e3aa"
    )


def cancel_all_orders():
    client_handler = Client()
    return client_handler.cancel_all_orders()
