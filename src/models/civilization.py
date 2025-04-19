from enum import Enum
from dataclasses import dataclass
from src.models.units.archer import Archer
from src.models.units.knight import Knight
from src.models.units.pikeman import Pikeman
from src.models.unit import Unit
from typing import List

@dataclass
class CivilizationArmyDistribution:
    """
    Distribution of units in a civilization
    """
    pikeman: int
    archer: int
    knight: int

class Civilization(Enum):
    """
    Enum representing different civilizations and their army distributions
    """
    CHINESE = CivilizationArmyDistribution(2, 25, 2)
    ENGLISH = CivilizationArmyDistribution(10, 10, 10)
    BIZANTINE = CivilizationArmyDistribution(5, 8, 15)

    def create_army(self) -> List[Unit]:
        """
        Creates an army based on the civilization's army distribution

        :return: List of units in the army
        :rtype: List[Unit]
        """
        distribution = self.value
        return (
            [Pikeman() for _ in range(distribution.pikeman)]+
            [Knight() for _ in range(distribution.knight)]+
            [Archer() for _ in range(distribution.archer)]
        )

    def __str__(self)-> str:
        """
        Returns the name of the civilization
        
        :return: Name of the civilization
        :rtype: str
        """
        return self.name.capitalize()