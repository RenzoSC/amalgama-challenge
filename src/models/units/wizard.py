from src.models.unit import Unit
from src.settings import WIZARD

class Wizard(Unit):
    """
    Wizard unit
    """
    default_base_strength = 50
    default_training_increment = 20

    def __init__(self):
        super().__init__()

    @property
    def type_name(self) -> str:
        return WIZARD