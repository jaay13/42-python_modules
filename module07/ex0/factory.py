from abc import ABC, abstractmethod

from .creature import Creature


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> Creature:
        """This will need to return a base form pokemon"""

    @abstractmethod
    def create_evolved(self) -> Creature:
        """This will need to return an evolved form pokemon"""
