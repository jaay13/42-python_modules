from abc import ABC, abstractmethod


class Creature(ABC):
    """Abstract base for all Creatures: shared name/type state, describe()."""

    def __init__(self, name: str, type: str) -> None:
        self._name = name
        self._type = type
        super().__init__()

    @abstractmethod
    def attack(self) -> str:
        """Return a string describing this Creature's attack."""

    def describe(self) -> str:
        """Return a standard message using the Creature's name and type."""
        return f"{self._name} is a {self._type} type Creature"
