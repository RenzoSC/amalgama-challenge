from src.models.army import Army
from src.models.civilization import Civilization
from src.services.transform import TransformationService
from src.services.training import TrainingService
from src.services.battle import BattleService
from random import uniform, choice
from src.exceptions import UnitNotFoundError
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    #Armies
    english = Army(Civilization.ENGLISH)
    english2 = Army(Civilization.ENGLISH)
    chinese = Army(Civilization.CHINESE)
    bizantine = Army(Civilization.BIZANTINE)
    armies = [english, english2, chinese, bizantine]
    logger.info(f"Armies: {armies}\n"+"-"*80)
    #english._Army__units = [] <-- Simulation - english army with no units

    #Training
    logger.info("Training units\n"+"-"*80)
    trains = int(uniform(1, 10))

    for _ in range(trains):
        army = choice(armies)
        random_unit = army.get_random_unit()
        if random_unit is None:
            logger.error(f"Army {army} has no units to train")
            continue
        n_times = int(uniform(1, 20))
        try:
            TrainingService.train_unit(random_unit, army, times=n_times)
        except UnitNotFoundError:
            logger.error(f"Unit {random_unit} not found in the army ({army}) units's array")
        except ValueError:
            logger.error(f"times ({n_times}) must be positive")

    # Battles
    logger.info("Battles\n"+"-"*80)

    BattleService.fight(english, chinese)
    BattleService.fight(chinese, english)
    BattleService.fight(english, english2)
    BattleService.fight(english, bizantine)

    # Transformations
    logger.info("Transformations\n"+"-"*80)

    transformations = int(uniform(1, 5))
    for _ in range(transformations):
        army = choice(armies)
        random_unit = army.get_random_unit()
        if random_unit is None:
            logger.error(f"Army {army} has no units to transform")
            continue
        try:
            TransformationService.transform_unit(random_unit, army)
        except UnitNotFoundError:
            logger.error(f"Unit {random_unit} not found in the army ({army}) units's array")
        except TypeError:
            logger.error(f"Unit {random_unit} cannot be transformed")

    # Second round of battles
    logger.info("Second round of battles\n"+"-"*80)

    BattleService.fight(english, chinese)
    BattleService.fight(bizantine, english2)
    BattleService.fight(chinese, bizantine)
    BattleService.fight(chinese, english2)

if __name__ == "__main__":
    main()