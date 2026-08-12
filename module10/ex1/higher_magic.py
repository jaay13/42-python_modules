"""Higher Realm: functions that take and return other functions.

Every spell follows the same contract:
    def spell(target: str, power: int) -> str
"""

from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    """Return a spell that casts both and returns a tuple of results.

    Both spells receive the same arguments.
    """

    def combined(target: str, power: int) -> tuple[str, str]:
        return spell1(target, power), spell2(target, power)

    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    """Return the same spell with its power multiplied before casting.

    The returned function keeps the original signature.
    """

    def amplified(target: str, power: int) -> str:
        return base_spell(target, multiplier * power)

    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    """Return a spell that only casts when condition is True.

    Condition and spell receive the same arguments; a failed
    condition returns "Spell fizzled".
    """

    def cast(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"

    return cast


def spell_sequence(spells: list[Callable]) -> Callable:
    """Return a spell that casts every spell in order.

    Each spell receives the same arguments; returns a list of all
    results.
    """

    def sequence(target: str, power: int) -> list[str]:
        res = []
        for spell in spells:
            res.append(spell(target, power))
        return res

    return sequence


def main() -> None:
    """Demonstrate each spell modifier."""

    def fire(target: str, power: int) -> str:
        return f"Fire wounded {target} for {power} HP"

    def heal(target: str, power: int) -> str:
        return f"Heal restores {target} for {power} HP"

    print("Testing spell combiner....")
    res = spell_combiner(fire, heal)("Wizard", 16)
    print(f"Combined spell result: {', '.join(res)}\n")

    print("Testing power amplifier...")
    normal = fire("Knight", 25)
    amplified = power_amplifier(fire, 2)("Knight", 25)
    print(f"Original: {normal}, Amplified: {amplified}\n")

    print("Testing conditional caster...")

    def enough_power(target: str, power: int) -> bool:
        return power > 50

    print(conditional_caster(enough_power, fire)("Dragon", 99))
    print(conditional_caster(enough_power, fire)("Dragon", 25))

    print("\nTesting spell sequencer...")
    print(spell_sequence([fire, heal])("Goblin", 25))


if __name__ == "__main__":
    main()
