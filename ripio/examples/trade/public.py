from ripio.trade.client import Client


def get_tickers():
    client_handler = Client()
    return client_handler.get_tickers()


def get_ticker_by_pair():
    client_handler = Client()
    return client_handler.get_ticker_by_pair("ETH_BRL")


def get_orderbook_level_3():
    client_handler = Client()
    return client_handler.get_orderbook_level_3(pair="BTC_BRL")


def get_orderbook_level_2():
    client_handler = Client()
    return client_handler.get_orderbook_level_2(pair="BTC_BRL")


def get_trades():
    client_handler = Client()
    return client_handler.get_trades()


def get_currencies():
    client_handler = Client()
    return client_handler.get_currencies()


def get_pairs():
    client_handler = Client()
    return client_handler.get_pairs()


def get_server_time():
    client_handler = Client()
    return client_handler.get_server_time()
