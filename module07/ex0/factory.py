from abc import ABC, abstractmethod

from .creature import Creature


class CreatureFactory(ABC):
    """Abstract factory creating a matched base/evolved Creature family."""

    @abstractmethod
    def create_base(self) -> Creature:
        """Return this family's base-form Creature."""

    @abstractmethod
    def create_evolved(self) -> Creature:
        """Return this family's evolved-form Creature."""
