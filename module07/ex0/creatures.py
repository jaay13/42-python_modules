from .creature import Creature


class Charmander(Creature):
    def attack(self) -> str:
        return f"{self._name} uses Ember!"


class Charizard(Creature):
    def attack(self) -> str:
        return f"{self._name} uses Flamethrower!"


class Squirtle(Creature):
    def attack(self) -> str:
        return f"{self._name} uses Water Gun!"


class Blastoise(Creature):
    def attack(self) -> str:
        return f"{self._name} uses Hydro Pump!"
