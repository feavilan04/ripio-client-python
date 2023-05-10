import datetime as dt
import json
from abc import ABC, abstractmethod
from json import JSONDecodeError

import requests
from eth_account import Account
from eth_account.messages import encode_defunct

import ripio
from ripio.exceptions.auth import UnathorizedClientException
from ripio.exceptions.response import NotSuccessfulResponseException


class RipioClient(ABC):
    # auth_mandatory = False
    _api_exception_manager = None

    # def __init_subclass__(cls, **kwargs):
    #     if cls.auth_mandatory:
    #         super().__init_subclass__(**kwargs)
    #     else:
    #         if "check_api_auth" in cls.__dict__:
    #             delattr(cls, "check_api_auth")
    #         super().__init_subclass__(**kwargs)

    def __init__(
        self,
        wallet_private_key,
        network,
        api_key=None,
        client_id=None,
        client_secret=None,
    ):
        self.session = requests.Session()
        self.__wallet_private_key = wallet_private_key
        self.network = network
        self.api_key = api_key
        self.client_id = client_id
        self.client_secret = client_secret

    # Client Manager Specific Methods

    def get_params_from_locals(self, local_vars, exclude_vars=[]):
        return {
            key: local_vars[key]
            for key in local_vars
            if key != "self"
            and local_vars[key] is not None
            and key not in exclude_vars
        }

    def process_arguments(self, *args, **kwargs):
        # process args
        args_list = [value for value in args]
        url_path = args_list[0]
        url = f"{ripio.BASE_URL}{url_path}"
        args_list[0] = url
        request_args = tuple(args_list)

        # process kwargs
        client_kwargs = {"success_status_code": kwargs["success_status_code"]}
        del kwargs["success_status_code"]
        request_kwargs = kwargs
        return request_args, request_kwargs, client_kwargs

    def process_response(self, response, client_kwargs):
        response_body = self.get_response_body(response)
        if "success_status_code" in client_kwargs:
            if response.status_code == client_kwargs["success_status_code"]:
                return response_body
            elif self._api_exception_manager is not None:
                self._api_exception_manager.dispatch(
                    response.status_code, response_body
                )
            else:
                message = f"{response.status_code} : {response_body}"
                raise NotSuccessfulResponseException(message)
        else:
            return response_body

    def get_response_body(self, response):
        try:
            json_body = response.json()
            if "data" in json_body and json_body.get("data") is not None:
                return json_body["data"]
            else:
                return json_body
        except JSONDecodeError:
            return response.text

    def remove_null_from_request_body(self, request_dict):
        return {
            key: value
            for key, value in request_dict.items()
            if value is not None
        }

    def check_api_key(func):
        def checker(self, *args, **kwargs):
            if self.api_key is None:
                raise UnathorizedClientException("No credentials were passed")
            self.authenticate_session()
            return func(self, *args, **kwargs)

        return checker

    def check_api_oauth(func):
        def checker(self, *args, **kwargs):
            if self.client_id is None:
                raise UnathorizedClientException("No client_id was passed")
            if self.client_secret is None:
                raise UnathorizedClientException("No client_secret was passed")
            self.authenticate_session()
            return func(self, *args, **kwargs)

        return checker

    # Destructor method to free up resources
    def __del__(self):
        self.session.close()

    # Abstract method used to enabled children implent their own Authentication
    # Over the session
    @abstractmethod
    def authenticate_session(self):
        pass

    # HTTP supported methods handlers
    def get(self, *args, **kwargs):
        request_args, request_kwargs, client_kwargs = self.process_arguments(
            *args, **kwargs
        )
        req = requests.Request("GET", *request_args, **request_kwargs)
        response = self.prepare_request(req)
        return self.process_response(response, client_kwargs)

    def put(self, *args, **kwargs):
        request_args, request_kwargs, client_kwargs = self.process_arguments(
            *args, **kwargs
        )
        req = requests.Request("PUT", *request_args, **request_kwargs)
        response = self.prepare_request(req)
        return self.process_response(response, client_kwargs)

    def post(self, *args, **kwargs):
        request_args, request_kwargs, client_kwargs = self.process_arguments(
            *args, **kwargs
        )
        req = requests.Request("POST", *request_args, **request_kwargs)
        response = self.prepare_request(req)
        return self.process_response(response, client_kwargs)

    def delete(self, *args, **kwargs):
        request_args, request_kwargs, client_kwargs = self.process_arguments(
            *args, **kwargs
        )
        req = requests.Request("DELETE", *request_args, **request_kwargs)
        response = self.prepare_request(req)
        return self.process_response(response, client_kwargs)

    def prepare_request(self, req):
        req_prepared = self.session.prepare_request(req)

        current_timestamp = str(int(dt.datetime.now().timestamp()))
        body = req_prepared.body if req_prepared.body is not None else ""

        # prepare request to send the request signed
        message = {
            "method": req_prepared.method,
            "request_body": body,
            "path": req_prepared.path_url,
            "timestamp": current_timestamp,
            "network": self.network,
        }

        # Add API KEY into the message if a Valid API KEY was passed
        if self.api_key is not None:
            message["api_key"] = self.api_key

        # Add API CLIENT ID into the message if a Valid client id was passed
        if self.client_id is not None:
            message["client_id"] = self.client_id

        # Add API CLIENT ID into the message if a Valid client id was passed
        if self.client_secret is not None:
            message["client_secret"] = self.client_secret

        # Dict must be sorted ASC to get same order as input hashed
        message_keys = list(message.keys())
        message_keys.sort()
        message_sorted = {i: message[i] for i in message_keys}

        message_string = json.dumps(message_sorted)

        # Hash the information
        message_hashed = encode_defunct(text=message_string)

        # Account creation from private key
        account = Account.from_key(self.__wallet_private_key)
        public_address = account.address
        signature = Account.sign_message(message_hashed, account.key)
        signature_string = signature.signature.hex()

        req_prepared.headers["X-RIPIO-SDK-TIMESTAMP"] = current_timestamp
        req_prepared.headers["X-RIPIO-SDK-SIGNATURE"] = signature_string
        req_prepared.headers["X-RIPIO-SDK-PUBLIC-ADDRESS"] = public_address
        req_prepared.headers["X-RIPIO-SDK-RPC-NETWORK"] = self.network

        response = self.session.send(req_prepared)

        return response
