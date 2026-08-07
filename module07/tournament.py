from ex0 import AquaFactory, CreatureFactory, FlameFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    AggressiveStrategy,
    BattleStrategy,
    DefensiveStrategy,
    InvalidStrategyError,
    NormalStrategy,
)


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    

if __name__ == "__main__":
    aqua_factory = AquaFactory()
    flame_factory = FlameFactory()

    healing_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()

    aggressive = AggressiveStrategy()
    defensive = DefensiveStrategy()
    normal = NormalStrategy()
