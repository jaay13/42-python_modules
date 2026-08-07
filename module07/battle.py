from ex0 import AquaFactory, CreatureFactory, FlameFactory


def test_factory(factory: CreatureFactory) -> None:
    """Verify a factory's base and evolved Creature can describe and attack."""
    print("Testing factory")

    creature_base = factory.create_base()
    creature_evolv = factory.create_evolved()

    creatures = [creature_base, creature_evolv]

    for creature in creatures:
        print(creature.describe())
        print(creature.attack())


def test_battle(flame: FlameFactory, aqua: AquaFactory) -> None:
    """Make two factories' base Creatures describe themselves and fight."""
    print("Testing battle")

    flame_base = flame.create_base()
    aqua_base = aqua.create_base()

    print(flame_base.describe())
    print(" vs.")
    print(aqua_base.describe())
    print(" fight!")

    print(flame_base.attack())
    print(aqua_base.attack())


if __name__ == "__main__":
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()

    test_factory(flame_factory)
    print()
    test_factory(aqua_factory)
    print()
    test_battle(flame_factory, aqua_factory)
