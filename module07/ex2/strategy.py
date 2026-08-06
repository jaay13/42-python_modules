from abc import ABC, abstractmethod

from ex0.creature import Creature

from .exceptions import InvalidStrategyError


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: Creature) -> None:
        """Will be called by the tournament script"""

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        """Return whether a Creature is suitable for this strategy"""

    def _check_valid(self, creature: Creature) -> None:
        """Raise InvalidStrategyError if the Creature isn't suitable"""
        if not self.is_valid(creature):
            strategy_label = type(self).__name__.removesuffix("Strategy").lower()
            raise InvalidStrategyError(creature._name, strategy_label)
