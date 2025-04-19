from src.models.army import Army
from src.exceptions import UnitNotFoundError, InvalidAmountError
import logging

logger = logging.getLogger(__name__)

class BattleService():
    WINNING_GOLD_REWARD = 100
    UNITS_LOST_ONE_WINNER = 2
    UNITS_LOST_DRAW = 1

    @staticmethod
    def fight(attacker:Army, defender: Army):
        """
        Simulates a battle between two armies

        :param attacker: The attacking army
        :param defender: The defending army
        """
        logger.info(f"Battle between {attacker} and {defender}")

        attacker_strength = attacker.total_strength
        defender_strength = defender.total_strength

        if attacker_strength > defender_strength:
            BattleService.apply_results_one_winner(attacker, defender)

        elif attacker_strength < defender_strength:
            BattleService.apply_results_one_winner(defender, attacker)

        else:
            BattleService.apply_results_draw(attacker, defender)
        
    @staticmethod
    def apply_results_one_winner(winner: Army, loser: Army):
        """
        Applies the result of a battle where one side wins

        :param winner: The winning army
        :param loser: The losing army

        :raises UnitNotFoundError: If the unit that is to be removed is not found in the army
        :raises InvalidAmountError: If the amount of gold to add is not positive
        """
        logger.info(f"Battle result: {winner} wins against {loser}")

        lost = loser.get_n_strongest_units(BattleService.UNITS_LOST_ONE_WINNER)
       
        for u in lost:
            try:
                loser.remove_unit(u)
            except UnitNotFoundError:
                logger.error(f"Unit {u} not found in the army ({loser}) units's array")

        try:
            winner.add_gold(BattleService.WINNING_GOLD_REWARD)
        except InvalidAmountError:
            logger.error(f"Invalid amount of gold ({BattleService.WINNING_GOLD_REWARD}) to add to the winner army")

        winner.record_battle(opponent=loser, won=True)
        loser.record_battle(opponent=winner, won=False)

    @staticmethod
    def apply_results_draw(attacker: Army, defender: Army):
        """
        Applies the result of a battle that ends in a draw

        :param attacker: The attacking army
        :param defender: The defending army

        :raises UnitNotFoundError: If the unit that is to be removed is not found in the army
        """
        logger.info(f"Battle result: {attacker} and {defender} draw")

        armies = [attacker, defender]

        for army in armies:
            units = army.get_n_strongest_units(BattleService.UNITS_LOST_DRAW)
            for u in units:
                try:
                    army.remove_unit(u)
                except UnitNotFoundError:
                    logger.error(f"Unit {u} not found in the army ({army}) units's array")
                    
        attacker.record_battle(opponent=defender, won=False)
        defender.record_battle(opponent=attacker, won=False)