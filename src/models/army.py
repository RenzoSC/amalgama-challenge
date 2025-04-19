from src.models.civilization import Civilization
from typing import List
from src.models.unit import Unit
from src.exceptions import UnitNotFoundError, DuplicateUnitError, InsufficientGoldError, InvalidAmountError
from random import choice
import secrets

class Army:
    """
    Represents a civilization's army
    """
    def __init__(self, civilization: Civilization):
        self.__civilization = civilization
        self.__units: List[Unit] = self.__civilization.create_army()
        self.__gold: int = 1000
        self.__battle_history: List[dict] = []
        self.__id = secrets.token_hex(5)

    @property
    def units(self) -> List[Unit]:
        """
        Gets the list of units in the army

        :return: List of units
        :rtype: List[Unit]
        """
        return self.__units

    @property
    def total_strength(self) -> int:
        """
        Calculates the total strength of the army

        :return: Total strength of the army
        :rtype: int
        """
        return sum(unit.strength for unit in self.__units)
    
    @property
    def gold(self) -> int:
        """
        Gets the amount of gold

        :return: Amount of gold
        :rtype: int
        """
        return self.__gold

    def spend_gold(self, amount : int):
        """
        Spends gold from the army
        
        :param amount: Amount of gold to spend (must be positive)
        
        :raises InvalidAmountError: If the amount is not positive
        :raises InsufficientGoldError: If the amount is greater than the available gold
        """
        if amount <= 0:
            raise InvalidAmountError("Amount must be positive")
        if amount > self.__gold:
            raise InsufficientGoldError("Not enough gold")
        
        self.__gold -= amount
    
    def add_gold(self, amount: int):
        """
        Adds gold to the army
        
        :param amount: Amount of gold to add (must be positive)
        
        :raises InvalidAmountError: If the amount is not positive
        """
        if amount <= 0:
            raise InvalidAmountError("Amount must be positive")
        self.__gold += amount
    
    def remove_unit(self, unit: Unit):
        """
        Removes a unit from the army
        
        :param unit: Unit to remove
        
        :raises UnitNotFoundError: If the unit is not found in the army
        """
        if unit not in self.__units:
            raise UnitNotFoundError("Unit not found in the army units's array")
        self.__units.remove(unit)
    
    def add_unit(self, unit: Unit):
        """
        Adds a unit to the army
        
        :param unit: Unit to add
        
        :raises DuplicateUnitError: If the unit is already in the army
        """
        if unit in self.__units:
            raise DuplicateUnitError("Unit already in the army units's array")
        self.__units.append(unit)

    def get_n_strongest_units(self, amount: int) -> List[Unit]:
        """
        Gets the n strongest units in the army
        
        :param amount: Number of strongest units to get (must be positive)
        
        :return: List of the n strongest units
        :rtype: List[Unit]
        """
        if amount <= 0:
            raise InvalidAmountError("Amount must be positive")
        sorted_units = sorted(self.__units, key=lambda unit: unit.strength)
        return sorted_units[:amount]
    
    def get_random_unit(self)-> Unit | None:
        """
        Gets a random unit from the army

        :return: Random unit or None if the army is empty
        :rtype: Unit | None
        """
        if not self.__units:
            return None
        return choice(self.__units)

    def record_battle(self, opponent: 'Army', won: bool):
        """
        Records the result of a battle

        :param opponent: The opponent army
        :param won: True if the army won, False otherwise
        """
        self.__battle_history.append({
            'opponent': opponent,
            'won': won
        })

    def __str__(self) ->str:
        """
        String representation of the army

        :return: String representation of the army
        :rtype: str
        """
        return f"{self.__civilization}-{self.__id}"
    
    def __repr__(self) ->str:
        """
        String representation of the army for debugging
        
        :return: String representation of the army
        :rtype: str
        """
        return str(self)