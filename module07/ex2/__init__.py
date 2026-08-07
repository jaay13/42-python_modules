"""Abstract strategy pattern: battle behaviors decoupled from Creature type."""

from .exceptions import InvalidStrategyError
from .strategies import AggressiveStrategy, DefensiveStrategy, NormalStrategy
from .strategy import BattleStrategy

__all__ = [
    "AggressiveStrategy",
    "BattleStrategy",
    "DefensiveStrategy",
    "InvalidStrategyError",
    "NormalStrategy"
]
