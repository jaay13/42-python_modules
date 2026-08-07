from ex0 import CreatureFactory

from .creatures import Bulbasaur, Venusaur, Zoroark, Zorua


class HealingCreatureFactory(CreatureFactory):
    """Factory for the Grass-type healing family (Bulbasaur/Venusaur)."""

    def create_base(self) -> Bulbasaur:
        return Bulbasaur("Bulbasaur", "Grass")

    def create_evolved(self) -> Venusaur:
        return Venusaur("Venusaur", "Grass/Poison")


class TransformCreatureFactory(CreatureFactory):
    """Factory for the Dark-type transform family (Zorua/Zoroark)."""

    def create_base(self) -> Zorua:
        return Zorua("Zorua", "Dark")

    def create_evolved(self) -> Zoroark:
        return Zoroark("Zoroark", "Dark")
