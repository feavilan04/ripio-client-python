class NotSuccessfulResponseException(Exception):
    pass


class NotFoundException(Exception):
    pass


class ExceededRequestLimitException(Exception):
    pass


class InternalServerErrorException(Exception):
    pass


class UnableToRetrieveDataException(Exception):
    pass


class ExternalCommunicationErrorException(Exception):
    pass


class InternalCommunicationErrorException(Exception):
    pass


class ServiveUnavailableException(Exception):
    pass
