import datetime as dt

import ripio
from ripio.examples import get_random_api_key
from ripio.trade.client import Client

mock_api_key = get_random_api_key()

# Using global api_key setting
ripio.api_key = mock_api_key


def get_user_balances():
    client_handler = Client()
    return client_handler.get_user_balances()


def get_user_balance_on_date():
    client_handler = Client()
    return client_handler.get_user_balance_on_date(dt.date(2023, 1, 26))


def get_user_fee_and_limits():
    client_handler = Client()
    return client_handler.get_user_fee_and_limits()


def get_user_statement():
    client_handler = Client()
    return client_handler.get_user_statement()


def get_user_statement_by_currency():
    client_handler = Client()
    return client_handler.get_user_statement_by_currency("BTC")


def get_user_trades():
    client_handler = Client()
    return client_handler.get_user_trades()
