from src.models.unit import Unit
from src.settings import KNIGHT

class Knight(Unit):
    """
    Knight unit
    """
    default_base_strength = 20
    default_training_increment = 10

    def __init__(self, base_strength: int = None):
        super().__init__(base_strength)

    @property
    def type_name(self) -> str:
        return KNIGHT