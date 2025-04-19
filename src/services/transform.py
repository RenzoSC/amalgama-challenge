from src.models.army import Army
from src.models.unit import Unit
from src.models.units.archer import Archer
from src.models.units.knight import Knight
from src.settings import PIKEMAN, ARCHER, KNIGHT, WIZARD
from src.exceptions import UnitNotFoundError, InvalidAmountError, InsufficientGoldError, DuplicateUnitError, UnitNotFoundError
import logging

logger = logging.getLogger(__name__)

class TransformationService:
    TRANSFORM_RULES = {
        PIKEMAN: (Archer, 30),
        ARCHER: (Knight, 40),
        KNIGHT: (None, 0),
        WIZARD: (None, 0)
    }
    
    @staticmethod
    def transform_unit(unit: Unit, army: Army):
        """
        Transforms a unit in the army
        
        :param unit: Unit to be transformed
        :param army: Army to which the unit belongs
        
        :raises UnitNotFoundError: If the unit is not found in the army
        :raises InvalidAmountError: If the amount of gold to spend is not positive
        :raises InsufficientGoldError: If the army does not have enough gold
        :raises TypeError: If the unit cannot be transformed
        :raises DuplicateUnitError: If the new unit is already in the army
        """
        logger.info(f"Transforming unit {unit} in army {army}")
        
        if unit not in army.units:
            raise UnitNotFoundError("Unit not found in the army units's array")
        
        target_type, cost = TransformationService.TRANSFORM_RULES[unit.type_name]
        if not target_type:
            raise TypeError(f"Unit {unit.type_name} cannot be transformed")
        
        try:
            army.spend_gold(cost)
            new_unit = target_type()
            army.remove_unit(unit)
            army.add_unit(new_unit)
            return new_unit
        except InvalidAmountError:
            logger.error(f"Invalid amount ({cost}) of gold to spend for training")
        except InsufficientGoldError:
            logger.error("Not enough gold to train the unit")
        except UnitNotFoundError:
            logger.error(f"Unit {unit} not found in the army ({army}) units's array")
        except DuplicateUnitError:
            logger.error(f"Unit {new_unit} already in the army ({army}) units's array")
            