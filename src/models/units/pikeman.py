from src.models.unit import Unit
from src.settings import PIKEMAN

class Pikeman(Unit):
    """
    Pikeman unit
    """
    default_base_strength = 5
    default_training_increment = 3
    def __init__(self):
        super().__init__()

    @property
    def type_name(self) -> str:
        return PIKEMAN