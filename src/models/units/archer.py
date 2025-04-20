from src.models.unit import Unit
from src.settings import ARCHER

class Archer(Unit):
    """
    Archer unit
    """
    default_base_strength = 10
    default_training_increment = 7
    def __init__(self):
        super().__init__()

    @property
    def type_name(self) -> str:
        return ARCHER
    