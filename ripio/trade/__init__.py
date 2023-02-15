from ripio.exceptions import ErrorDispatcherInterface
from ripio.exceptions.auth import (
    ForbiddenAccessException,
    UnathorizedClientException,
)
from ripio.exceptions.request import InvalidParamatersException
from ripio.exceptions.response import (
    ExceededRequestLimitException,
    ExternalCommunicationErrorException,
    InternalCommunicationErrorException,
    InternalServerErrorException,
    NotFoundException,
    NotSuccessfulResponseException,
    ServiveUnavailableException,
    UnableToRetrieveDataException,
)

from .exceptions import (
    BlockedWitdrawalsException,
    InsufficientFundsException,
    NoOrdersToCancelException,
    OrderAlreadyCanceledException,
    OrderAmountBelowMinimumsException,
    PreventionDuplicateWithdrawalException,
    TemporaryBlockedWithdrawalsException,
    TFANotEnabledException,
    UnexistentDestinationAccountException,
    UnsupportedOperation,
    WalletCreationMinimumAmountNotReachedException,
    WalletDestinationNotAuthorizedException,
    WithdrawalAmountBelowMinimumException,
    WithdrawalLimitExceededException,
)


class TradeErrorDispatcher(ErrorDispatcherInterface):
    @staticmethod
    def dispatch(http_status_code, response_body):
        print(http_status_code, response_body)
        http_code = str(http_status_code)
        message = ""
        error_code = ""
        if isinstance(response_body, dict):
            message = response_body.get("message")
            error_code = response_body.get("error_code")

        # 400 Errors
        if http_code == "400":
            if error_code == "40010":
                raise OrderAmountBelowMinimumsException(message)
            elif error_code == "40011":
                raise InsufficientFundsException(message)
            elif error_code == "40020":
                raise OrderAlreadyCanceledException(message)
            elif error_code == "40021":
                raise NoOrdersToCancelException(message)
            elif error_code == "40030":
                raise WithdrawalLimitExceededException(message)
            elif error_code == "40031":
                raise WithdrawalAmountBelowMinimumException(message)
            elif error_code == "40032":
                raise PreventionDuplicateWithdrawalException(message)
            elif error_code == "40033":
                raise WalletDestinationNotAuthorizedException(message)
            elif error_code == "40034":
                raise UnexistentDestinationAccountException(message)
            elif error_code == "40035":
                raise WalletCreationMinimumAmountNotReachedException(message)
            elif error_code == "40040":
                raise TemporaryBlockedWithdrawalsException(message)
            elif error_code == "40041":
                raise BlockedWitdrawalsException(message)
            elif error_code == "40050":
                raise TFANotEnabledException(message)
            elif error_code == "40090":
                raise UnsupportedOperation(message)
            else:
                raise InvalidParamatersException(message)

        # 401 error
        elif http_code == "401":
            raise UnathorizedClientException(message)

        # 403 error
        elif http_code == "403":
            raise ForbiddenAccessException(message)

        # 404 error
        elif http_code == "404":
            raise NotFoundException(message)

        # 429 error
        elif http_code == "429":
            raise ExceededRequestLimitException(message)

        # 500 error
        elif http_code == "500":
            if error_code == "50001":
                raise UnableToRetrieveDataException(message)
            elif error_code == "50002":
                raise ExternalCommunicationErrorException(message)
            elif error_code == "50003":
                raise InternalCommunicationErrorException(message)
            else:
                raise InternalServerErrorException(message)

        # 503 error
        elif http_code == "503":
            raise ServiveUnavailableException(message)

        # Default error exception
        else:
            raise NotSuccessfulResponseException(message)
