from ex0.creature import Creature
from ex1.capability import HealCapability, TransformCapability

from .strategy import BattleStrategy


class NormalStrategy(BattleStrategy):
    def act(self, creature: Creature):
        print(creature.attack())

    def is_valid(self):
        return True

class AggressiveStrategy(BattleStrategy):
    pass # WIP