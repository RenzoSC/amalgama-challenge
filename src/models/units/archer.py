from src.models.unit import Unit
from src.settings import ARCHER

class Archer(Unit):
    """
    Archer unit
    """
    default_base_strength = 10
    default_training_increment = 7
    def __init__(self, base_strength: int = None):
        super().__init__(base_strength)

    @property
    def type_name(self) -> str:
        return ARCHER
    