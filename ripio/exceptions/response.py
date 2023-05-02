from ripio.exceptions import RipioException


class NotSuccessfulResponseException(RipioException):
    pass


class NotFoundException(RipioException):
    pass


class ExceededRequestLimitException(RipioException):
    pass


class InternalServerErrorException(RipioException):
    pass


class UnableToRetrieveDataException(RipioException):
    pass


class ExternalCommunicationErrorException(RipioException):
    pass


class InternalCommunicationErrorException(RipioException):
    pass


class ServiveUnavailableException(RipioException):
    pass


class RequestTimeoutException(RipioException):
    pass
