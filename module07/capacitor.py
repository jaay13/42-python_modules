from ex1 import *



def test_healing(factory: HealingCreatureFactory) -> None:
    
    base = factory.create_base()
    evolved = factory.create_evolved()

    print(" base:")
    print(f"{base.describe()}")

    print(f"{base.attack()}")

    print(f"{base.heal()}")

    print(" evolved:")
    print(f"{evolved.describe()}")

    print(f"{evolved.attack()}")

    print(f"{evolved.heal()}")


def test_transform(factory: TransformCreatureFactory) -> None:
    
    base = factory.create_base()
    evolved = factory.create_evolved()

    print(" base:")
    print(f"{base.describe()}")

    print(f"{base.attack()}")

    print(f"{base.transform()}")

    print(f"{base.attack()}")

    print(f"{base.revert()}")

    print(" evolved:")
    print(f"{evolved.describe()}")

    print(f"{evolved.attack()}")

    print(f"{evolved.transform()}")

    print(f"{evolved.attack()}")

    print(f"{evolved.revert()}")




if __name__ == "__main__":
    print("Testing Creature with healing capability")
    heal_factory = HealingCreatureFactory()
    test_healing(heal_factory)

    print("\nTesting Creature with transform capability")
    transform_factory = TransformCreatureFactory()
    test_transform(transform_factory)