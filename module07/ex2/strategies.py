from ex0.creature import Creature
from ex1.capability import HealCapability, TransformCapability

from .strategy import BattleStrategy


class NormalStrategy(BattleStrategy):
    """Suitable for any Creature; simply attacks."""

    def act(self, creature: Creature) -> None:
        print(creature.attack())

    def is_valid(self, creature: Creature) -> bool:
        return True


class AggressiveStrategy(BattleStrategy):
    """Suitable for Creatures with transform capability; transforms,
    attacks, then reverts."""

    def act(self, creature: Creature) -> None:
        self._check_valid(creature)
        if isinstance(creature, TransformCapability):
            print(creature.transform())
            print(creature.attack())
            print(creature.revert())

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)


class DefensiveStrategy(BattleStrategy):
    """Suitable for Creatures with healing capability; attacks, then heals."""

    def act(self, creature: Creature) -> None:
        self._check_valid(creature)
        if isinstance(creature, HealCapability):
            print(creature.attack())
            print(creature.heal())

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)
