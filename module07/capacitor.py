from ex1 import HealingCreatureFactory, TransformCreatureFactory


def test_healing(factory: HealingCreatureFactory) -> None:
    """Verify a healing factory's Creatures can describe, attack, and heal."""
    base = factory.create_base()
    evolved = factory.create_evolved()

    print(" base:")
    print(base.describe())

    print(base.attack())

    print(base.heal())

    print(" evolved:")
    print(evolved.describe())

    print(evolved.attack())

    print(evolved.heal())


def test_transform(factory: TransformCreatureFactory) -> None:
    """Verify a transform factory's Creatures can describe, attack,
    transform, and revert."""
    base = factory.create_base()
    evolved = factory.create_evolved()

    print(" base:")
    print(base.describe())

    print(base.attack())

    print(base.transform())

    print(base.attack())

    print(base.revert())

    print(" evolved:")
    print(evolved.describe())

    print(evolved.attack())

    print(evolved.transform())

    print(evolved.attack())

    print(evolved.revert())


if __name__ == "__main__":
    print("Testing Creature with healing capability")
    heal_factory = HealingCreatureFactory()
    test_healing(heal_factory)

    print("\nTesting Creature with transform capability")
    transform_factory = TransformCreatureFactory()
    test_transform(transform_factory)
