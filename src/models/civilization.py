from enum import Enum
from dataclasses import dataclass
from src.models.units.archer import Archer
from src.models.units.knight import Knight
from src.models.units.pikeman import Pikeman

@dataclass
class CivilizationArmyDistribution:
    """
    Distribution of units in a civilization
    """
    pikeman: int
    archer: int
    knight: int

class Civilization(Enum):
    CHINESE = CivilizationArmyDistribution(2, 25, 2)
    ENGLISH = CivilizationArmyDistribution(10, 10, 10)
    BIZANTINE = CivilizationArmyDistribution(5, 8, 15)

    def create_army(self):
        """
        Create an army based on the civilization's army distribution
        """
        distribution = self.value
        return (
            [Pikeman() for _ in range(distribution.pikeman)]+
            [Knight() for _ in range(distribution.knight)]+
            [Archer() for _ in range(distribution.archer)]
        )

    def __str__(self):
        """
        Return the name of the civilization
        """
        return self.name.capitalize()