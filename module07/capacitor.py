from ex1 import *


def main() -> None:
    healing_factory = HealingCreatureFactory()
    base_heal = healing_factory.create_base()

    print("Testing Creature with healing capability")
    print(" base:")
    print(f"{base_heal.describe()}")

    print(f"{base_heal.attack()}")

    print(f"{base_heal.heal()}")
