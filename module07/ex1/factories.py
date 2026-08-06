from ex0 import CreatureFactory
from ex0.creature import Creature

from .creatures import Bulbasaur, Venusaur, Zoroark, Zorua


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Bulbasaur:
        return Bulbasaur("Bulbasaur", "Grass")

    def create_evolved(self) -> Venusaur:
        return Venusaur("Venusaur", "Grass/Poison")


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Zorua:
        return Zorua("Zorua", "Dark")

    def create_evolved(self) -> Zoroark:
        return Zoroark("Zoroark", "Dark")
