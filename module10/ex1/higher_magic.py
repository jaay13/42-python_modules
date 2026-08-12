"""Higher Realm: functions that take and return other functions.

Every spell follows the same contract:
    def spell(target: str, power: int) -> str
"""

from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    """Return a spell that casts both and returns a tuple of results.

    Both spells receive the same arguments.
    """
    raise NotImplementedError


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    """Return the same spell with its power multiplied before casting.

    The returned function keeps the original signature.
    """
    raise NotImplementedError


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    """Return a spell that only casts when condition is True.

    Condition and spell receive the same arguments; a failed
    condition returns "Spell fizzled".
    """
    raise NotImplementedError


def spell_sequence(spells: list[Callable]) -> Callable:
    """Return a spell that casts every spell in order.

    Each spell receives the same arguments; returns a list of all
    results.
    """
    raise NotImplementedError


def main() -> None:
    """Demonstrate each spell modifier."""
    raise NotImplementedError


if __name__ == "__main__":
    main()
