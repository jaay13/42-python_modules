from ex0.creature import Creature

from .capability import HealCapability, TransformCapability


class Bulbasaur(Creature, HealCapability):
    def attack(self) -> str:
        return f"{self._name} uses Vine Whip!"

    def heal(self) -> str:
        return f"{self._name} heals itself for a small amount"


class Venusaur(Creature, HealCapability):
    def attack(self) -> str:
        return f"{self._name} uses Petal Dance!"

    def heal(self) -> str:
        return f"{self._name} heals itself and others for a large amount"


class Zorua(Creature, TransformCapability):
    def attack(self) -> str:
        """Attack normally, or with a boosted move if transformed."""
        if not self._transformed:
            return f"{self._name} uses Scratch!"
        else:
            return f"{self._name} uses Night Slash! (transformed attack)"

    def transform(self) -> str:
        self._transformed = True
        return (
            f"{self._name} activates Illusion and disguises "
            "as a fiercer-looking Pokemon"
        )

    def revert(self) -> str:
        self._transformed = False
        return (
            f"{self._name}'s Illusion breaks and reveals "
            "it's true form again"
        )


class Zoroark(Creature, TransformCapability):
    def attack(self) -> str:
        """Attack normally, or with a boosted move if transformed."""
        if not self._transformed:
            return f"{self._name} uses Sucker Punch!"
        else:
            return f"{self._name} uses Night Daze! (transformed attack)"

    def transform(self) -> str:
        self._transformed = True
        return (
            f"{self._name} activates Illusion and takes "
            "on a more menacing form"
        )

    def revert(self) -> str:
        self._transformed = False
        return (
            f"{self._name}'s Illusion fades and reveals "
            "it's true form again"
        )
