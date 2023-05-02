import ripio
from ripio.examples import get_random_api_key
from ripio.trade.client import Client

random_api_key = get_random_api_key()

"""
There are two possible ways to authenticate for the API

- Set global api_key for Ripio (Uses the same API key for all
the connections to any of the products on the SDK)
- Specific api_key for a custom product
"""

# Global configuration
ripio.api_key = random_api_key

# All the SDK calls to any of the products will
# use ripio.api_key as the authetication key


# Custom API key for product

trade_client = Client(random_api_key)

"""
NOTE: If a global api_key is specified and a custom api_key is
specified for a certain product, The custom product will
override the global api_key for that product
"""
