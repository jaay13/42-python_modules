"""Ancient Library: reduce, partial, lru_cache and singledispatch."""

from collections.abc import Callable
from functools import lru_cache, partial, reduce, singledispatch
from operator import add, mul
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    """Combine all spell powers with functools.reduce.

    Supports "add", "multiply", "max" and "min", using the operator
    module where one fits. Returns 0 for an empty list, and handles
    an unknown operation rather than failing silently.
    """

    if not spells:
        return 0
    if operation == "add":
        return reduce(add, spells)
    elif operation == "multiply":
        return reduce(mul, spells)
    elif operation == "max":
        return reduce(max, spells)
    elif operation == "min":
        return reduce(min, spells)
    else:
        raise ValueError("Wrong operation provided")


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    """Build three specialised enchantments with functools.partial.

    base_enchantment has the signature
    (power: int, element: str, target: str) -> str; each version
    pre-fills power=50 and one element.
    """
    sharpess_enchant = partial(base_enchantment, 50, "Sharpness")
    smite_enchant = partial(base_enchantment, 50, "Smite")
    bane_of_arthropods_enchant = partial(
        base_enchantment, 50, "Bane_of_arthropods"
    )

    return {
        "sharpness": sharpess_enchant,
        "smite": smite_enchant,
        "bane_of_arthropods": bane_of_arthropods_enchant
    }


@lru_cache
def memoized_fibonacci(n: int) -> int:
    """Return the nth Fibonacci number, cached with lru_cache.

    lru_cache memoizes each (n -> result) pair the first time it's
    computed, so repeated or overlapping recursive calls with the
    same n are served from cache instead of recomputed, turning the
    naive exponential-time recursion into linear time.

    Caching is observable through memoized_fibonacci.cache_info().
    """
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    """Return a functools.singledispatch spell caster.

    singledispatch turns one function into a type-based switch: the
    @singledispatch-decorated function 'fallback' is the fallback for any type
    with no registered handler, and each @fallback.register(SomeType)
    adds a handler that fires instead whenever the first argument's
    runtime type matches SomeType. The fallback implementation handles
    unknown types; int casts damage, str enchants, and list
    multi-casts.
    """
    @singledispatch
    def fallback(spell: Any) -> str:
        return "Unknown spell type"

    @fallback.register(int)
    def integers(n: int) -> str:
        return f"Damage spell: {n} damage"

    @fallback.register(str)
    def strings(spell: str) -> str:
        return f"Enchantment: {spell}"

    @fallback.register(list)
    def lists(spell: list) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return fallback


def main() -> None:
    """Demonstrate each functools artifact."""
    raise NotImplementedError


if __name__ == "__main__":
    main()
