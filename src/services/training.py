from src.models.army import Army
from src.models.unit import Unit
from src.settings import PIKEMAN, ARCHER, KNIGHT
from src.exceptions import UnitNotFoundError, InvalidAmountError, InsufficientGoldError
import logging

logger = logging.getLogger(__name__)

class TrainingService:
    TRAINING_COSTS = {
        PIKEMAN:  10,
        ARCHER:  20,
        KNIGHT:  30
    }
    
    @staticmethod
    def train_unit(unit: Unit, army: Army, times: int = 1):
        """
        Trains a unit in the army
        
        :param unit: Unit to be trained
        :param army: Army to which the unit belongs
        :param times: Number of times to train the unit (default is 1)
        
        :raises UnitNotFoundError: If the unit is not found in the army
        :raises InvalidAmountError: If the amount of times is not positive or total cost is not positive
        :raises InsufficientGoldError: If the army does not have enough gold
        """
        if unit not in army.units:
            raise UnitNotFoundError(f"Unit {unit} not found in the army ({army}) units's array")
        if times <= 0:
            raise InvalidAmountError(f"times ({times}) must be positive")

        cost_per = TrainingService.TRAINING_COSTS[unit.type_name]
        total_cost = cost_per * times
        try:
            army.spend_gold(total_cost)
        except InvalidAmountError:
            logger.error(f"Invalid amount ({total_cost}) of gold to spend for training")
            return
        except InsufficientGoldError:
            logger.error("Not enough gold to train the unit")
            return
        
        for _ in range(times):
            unit.train()
