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

    tournament_0 = [
        (flame_factory, normal)
        (healing_factory, defensive)
    ]
    print("Tournament 0 (basic)")
    battle(tournament_0)

    tournament_1 = [
        (flame_factory, aggressive)
        (healing_factory, defensive)
    ]
    print("Tournament 1 (error)")
    battle(tournament_1)

    tournament_2 = [
        (aqua_factory, normal)
        (healing_factory, defensive)
        (transform_factory, aggressive)
    ]
    print("Tournament 2 (multiple battles)")
    battle(tournament_2)
