from ripio.exceptions import RipioException


class UnathorizedClientException(RipioException):
    pass


class ForbiddenAccessException(RipioException):
    pass
