from abc import ABC, abstractstaticmethod


class ErrorDispatcherInterface(ABC):
    @abstractstaticmethod
    def dispatch(http_status_code, response_body):
        pass


class RipioException(Exception):
    pass
