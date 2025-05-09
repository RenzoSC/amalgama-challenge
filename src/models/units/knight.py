from src.models.unit import Unit
from src.settings import KNIGHT

class Knight(Unit):
    """
    Knight unit
    """
    default_base_strength = 20
    default_training_increment = 10

    def __init__(self):
        super().__init__()

    @property
    def type_name(self) -> str:
        return KNIGHT