class OrderAmountBelowMinimumsException(Exception):
    pass

class InsufficientFundsException(Exception):
    pass

class OrderAlreadyCanceledException(Exception):
    pass

class NoOrdersToCancelException(Exception):
    pass 

class WithdrawalLimitExceededException(Exception):
    pass

class WithdrawalAmountBelowMinimumException(Exception):
    pass

class PreventionDuplicateWithdrawalException(Exception):
    pass

class WalletDestinationNotAuthorizedException(Exception):
    pass

class UnexistentDestinationAccountException(Exception):
    pass

class WalletCreationMinimumAmountNotReachedException(Exception):
    pass

class TemporaryBlockedWithdrawalsException(Exception):
    pass

class BlockedWitdrawalsException(Exception):
    pass

class TFANotEnabledException(Exception):
    pass

class UnsupportedOperation(Exception):
    pass

