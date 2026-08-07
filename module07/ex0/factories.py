from .creature import Creature
from .creatures import Blastoise, Charizard, Charmander, Squirtle
from .factory import CreatureFactory


class FlameFactory(CreatureFactory):
    """Factory for the Fire-type Charmander family."""

    def create_base(self) -> Creature:
        return Charmander("Charmander", "Fire")

    def create_evolved(self) -> Creature:
        return Charizard("Charizard", "Fire/Flying")


class AquaFactory(CreatureFactory):
    """Factory for the Water-type Squirtle family."""

    def create_base(self) -> Creature:
        return Squirtle("Squirtle", "Water")

    def create_evolved(self) -> Creature:
        return Blastoise("Blastoise", "Water")
