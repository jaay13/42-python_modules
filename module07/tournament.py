from ex0 import AquaFactory, CreatureFactory, FlameFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    AggressiveStrategy,
    BattleStrategy,
    DefensiveStrategy,
    InvalidStrategyError,
    NormalStrategy,
)


def run_tournament(
    header: str,
    description: str,
    opponents: list[tuple[CreatureFactory, BattleStrategy]]
) -> None:
    """Print a tournament's header, then run its battles."""
    print(header)
    print(description)
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    battle(opponents)


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    """Make every opponent fight each other exactly once.

    Each fighter uses its own paired BattleStrategy. An invalid
    Creature-strategy combination aborts the rest of this tournament.
    """
    for i, a in enumerate(opponents):
        for b in opponents[i + 1:]:
            factory_a, strategy_a = a
            factory_b, strategy_b = b

            creature_a = factory_a.create_base()
            creature_b = factory_b.create_base()

            print("\n* Battle *")
            print(creature_a.describe())
            print(" vs.")
            print(creature_b.describe())
            print(" now fight!")

            try:
                strategy_a.act(creature_a)
                strategy_b.act(creature_b)
            except InvalidStrategyError as e:
                print(f"Battle error, aborting tournament: {e}")
                return


if __name__ == "__main__":
    aqua_factory = AquaFactory()
    flame_factory = FlameFactory()

    healing_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()

    aggressive = AggressiveStrategy()
    defensive = DefensiveStrategy()
    normal = NormalStrategy()

    tournament_0 = [
        (flame_factory, normal),
        (healing_factory, defensive),
    ]

    run_tournament(
        "Tournament 0 (basic)",
        " [ (Charmander+Normal), (Healing+Defensive) ]",
        tournament_0
    )
    print()

    tournament_1 = [
        (flame_factory, aggressive),
        (healing_factory, defensive),
    ]

    run_tournament(
        "Tournament 1 (error)",
        " [ (Charmander+Aggressive), (Healing+Defensive) ]",
        tournament_1
    )
    print()

    tournament_2 = [
        (aqua_factory, normal),
        (healing_factory, defensive),
        (transform_factory, aggressive),
    ]

    run_tournament(
        "Tournament 2 (multiple battles)",
        " [ (Squirtle+Normal), (Healing+Defensive), (Transform+Aggressive) ]",
        tournament_2
    )
