from abc import ABC, abstractmethod
from src.exceptions import InvalidAmountError

class Unit(ABC):
    """
    Abstract base class for all units
    """
    default_base_strength: int
    default_training_increment: int

    def __init__(self):
        self.__strenght = self.default_base_strength
        self.__training_increment = self.default_training_increment

    @property
    @abstractmethod
    def type_name(self) -> str:
        ...

    @property
    def strenght(self) -> int:
        return self.__strenght
    
    def train(self, amount: int = None):
        adding = amount if amount else self.__training_increment
        if adding <= 0:
            raise InvalidAmountError("Amount must be positive")
        
        self.__strenght += adding
        return self.__strenght