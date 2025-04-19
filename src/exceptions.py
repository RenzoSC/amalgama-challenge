class InvalidAmountError(Exception):
    """Raised when an amount isn't valid (negative or zero)"""
    pass

class ArmyError(Exception):
    """Base class for exceptions in the Army module"""
    pass

class UnitNotFoundError(ArmyError):
    """Exception raised when an unit isn't in the army units's array"""
    pass

class DuplicateUnitError(ArmyError):
    """Exception raised when an unit is already in the army units's array"""
    pass

class InsufficientGoldError(ArmyError):
    """Raised when the army doesn't have enough gold"""
    pass

