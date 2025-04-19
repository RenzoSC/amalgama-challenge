from src.models.civilization import Civilization
from typing import List
from src.models.unit import Unit
from src.exceptions import UnitNotFoundError, DuplicateUnitError, InsufficientGoldError, InvalidAmountError

class Army:
    def __init__(self, civilization: Civilization):
        self.__civilization = civilization
        self.__units: List[Unit] = self.__civilization.create_army()
        self.__gold: int = 1000
        self.__battle_history: List[dict] = []

    @property
    def units(self) -> List[Unit]:
        """
        Get the list of units in the army
        """
        return self.__units

    @property
    def total_strength(self) -> int:
        """
        Calculate the total strength of the army
        """
        return sum(unit.strenght for unit in self.__units)
    
    @property
    def gold(self) -> int:
        """
        Get the amount of gold
        """
        return self.__gold

    def spend_gold(self, amount : int):
        if amount <= 0:
            raise InvalidAmountError("Amount must be positive")
        if amount > self.__gold:
            raise InsufficientGoldError("Not enough gold")
        
        self.__gold -= amount
    
    def add_gold(self, amount: int):
        if amount <= 0:
            raise InvalidAmountError("Amount must be positive")
        self.__gold += amount
    
    def remove_unit(self, unit: Unit):
        if unit not in self.__units:
            raise UnitNotFoundError("Unit not found in the army units's array")
        self.__units.remove(unit)
    
    def add_unit(self, unit: Unit):
        if unit in self.__units:
            raise DuplicateUnitError("Unit already in the army units's array")
        self.__units.append(unit)

    def get_n_strongest_units(self, amount: int) -> List[Unit]:
        if amount <= 0:
            raise InvalidAmountError("Amount must be positive")
        sorted_units = sorted(self.__units, key=lambda unit: unit.strenght)
        return sorted_units[:amount]

    def record_battle(self, opponent: 'Army', won: bool):
        """
        Record the result of a battle
        """
        self.__battle_history.append({
            'opponent': opponent,
            'won': won
        })
