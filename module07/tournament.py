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
                print(f"Battle error, aborting tournament: {e}\n")
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
    print("Tournament 0 (basic)")
    print(" [ (Charmander+Normal), (Bulbasaur+Defensive) ]")
    print("*** Tournament ***")
    print(f"{len(tournament_0)} opponents involved")
    battle(tournament_0)
    print()

    tournament_1 = [
        (flame_factory, aggressive),
        (healing_factory, defensive),
    ]
    print("Tournament 1 (error)")
    print(" [ (Charmander+Aggressive), (Bulbasaur+Defensive) ]")
    print("*** Tournament ***")
    print(f"{len(tournament_1)} opponents involved")
    battle(tournament_1)

    tournament_2 = [
        (aqua_factory, normal),
        (healing_factory, defensive),
        (transform_factory, aggressive),
    ]
    print("Tournament 2 (multiple battles)")
    print(" [ (Squirtle+Normal), (Bulbasaur+Defensive), (Zorua+Aggressive) ]")
    print("*** Tournament ***")
    print(f"{len(tournament_2)} opponents involved")
    battle(tournament_2)
