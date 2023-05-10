import datetime as dt

from ripio.core import RipioClient
from ripio.exceptions.request import InvalidParamatersException


class Client(RipioClient):
    def __init__(
        self, wallet_private_key, network, client_id=None, client_secret=None
    ):
        self.path = "b2b/"
        super().__init__(
            wallet_private_key,
            network,
            client_id=client_id,
            client_secret=client_secret,
        )

    def authenticate_session(self):
        self.session.headers["X-RIPIO-CLIENT-ID"] = self.client_id
        self.session.headers["X-RIPIO-CLIENT-SECRET"] = self.client_secret

    @RipioClient.check_api_oauth
    def get_reusable_quotes(self, pair=None, date_gt=None):
        if date_gt is not None:
            if not isinstance(date_gt, dt.date):
                raise InvalidParamatersException(
                    "'date_gt' must be a datetime.date instance"
                )
            date_gt = date_gt.isoformat()
        params = {"pair": pair, "date_gt": date_gt}
        params = self.get_params_from_locals(params)
        response = self.get(
            f"{self.path}reusable-quotes",
            params=params,
            success_status_code=200,
        )
        return response

    @RipioClient.check_api_oauth
    def create_reusable_quotes(self, pair, external_ref):
        body = {"pair": pair, "external_ref": external_ref}
        response = self.post(
            f"{self.path}reusable-quotes",
            json=body,
            success_status_code=200,
        )
        return response
