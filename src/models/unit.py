from abc import ABC, abstractmethod
from src.exceptions import InvalidAmountError
import secrets

class Unit(ABC):
    """
    Abstract base class for all units

    Subclasses must implement the type_name property and set the default_base_strength and default_training_increment attributes
    """
    default_base_strength: int
    default_training_increment: int

    def __init__(self):
        """
        Initializes the unit with default base strength and training increment
        """
        self.__strength = self.default_base_strength
        self.__training_increment = self.default_training_increment
        self.__id = secrets.token_hex(5)

    @property
    @abstractmethod
    def type_name(self) -> str:
        """
        The name of the unit (must be implemented by subclasses).
        
        :return: Name of the unit
        :rtype: str
        """
        ...

    @property
    def strength(self) -> int:
        """
        Current strength of the unit
        
        :return: Strength of the unit
        :rtype: int
        """
        return self.__strength
    
    def train(self, amount: int = None) -> int:
        """
        Trains the unit to increase its strength
        
        :param amount: Amount to increase the strength by (default is the training increment)
        
        :return: New strength of the unit
        :rtype: int

        :raises InvalidAmountError: If the amount is not positive
        """
        adding = amount if amount else self.__training_increment
        if adding <= 0:
            raise InvalidAmountError("Amount must be positive")
        
        self.__strength += adding
        return self.__strength
    
    def __str__(self) -> str:
        """
        String representation of the unit
        
        :return: String representation of the unit
        :rtype: str
        """
        return f"{self.type_name}-{self.__id}"