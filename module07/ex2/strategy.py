from abc import ABC, abstractmethod

from ex0.creature import Creature


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: Creature) -> None:
        """Will be called by the tournament script"""

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        """Will return a bool indicating that a Creature is suitable for strategy"""

    def _check_valid(self, creature: Creature) -> None:
        """Will return a bool indicating that """
        if not self.is_valid(creature):
            raise Exception()