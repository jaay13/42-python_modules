from abc import ABC, abstractmethod


class HealCapability(ABC):
    @abstractmethod
    def heal(self) -> str:
        """This will need to return a proper heal string"""

class TransformCapability(ABC):
    def __init__(self) -> None:
        self._transformed = False

    @abstractmethod
    def transform(self) -> str:
        """this will need to return a proper transform string"""

    @abstractmethod
    def revert(self) -> str:
        """This will need to return a proper revert string"""
