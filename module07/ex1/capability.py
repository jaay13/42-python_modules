from abc import ABC, abstractmethod


class HealCapability(ABC):
    """Mixin adding a heal ability, independent of the Creature hierarchy."""

    @abstractmethod
    def heal(self) -> str:
        """Return a string describing this Creature's healing action."""


class TransformCapability(ABC):
    """Mixin adding a transform/revert ability with persistent state.

    _transformed tracks whether the Creature is currently transformed,
    which impacts its attack() implementation.
    """

    def __init__(self) -> None:
        self._transformed = False

    @abstractmethod
    def transform(self) -> str:
        """Return a string describing this Creature's transformation."""

    @abstractmethod
    def revert(self) -> str:
        """Return a string describing this Creature reverting to normal."""
