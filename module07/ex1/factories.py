from ex0 import CreatureFactory
from ex0.creature import Creature

from .creatures import Bulbasaur, Venusaur, Zoroark, Zorua


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Bulbasaur("Bulbasaur", "Grass")

    def create_evolved(self) -> Creature:
        return Venusaur("Venusaur", "Grass/Poison")


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Zorua("Zorua", "Dark")

    def create_evolved(self) -> Creature:
        return Zoroark("Zoroark", "Dark")
