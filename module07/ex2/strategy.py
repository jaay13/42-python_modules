from abc import ABC, abstractmethod

from ex0.creature import Creature

from .exceptions import InvalidStrategyError


class BattleStrategy(ABC):
    """Abstract strategy for how a Creature behaves during a battle."""

    @abstractmethod
    def act(self, creature: Creature) -> None:
        """Perform this strategy's battle sequence on the given Creature."""

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        """Return whether a Creature is suitable for this strategy"""

    def _check_valid(self, creature: Creature) -> None:
        """Raise InvalidStrategyError if the Creature isn't suitable"""
        if not self.is_valid(creature):
            cls_name = type(self).__name__
            strategy_label = cls_name.removesuffix("Strategy").lower()
            raise InvalidStrategyError(creature._name, strategy_label)
