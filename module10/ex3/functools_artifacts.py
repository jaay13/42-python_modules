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


def memoized_fibonacci(n: int) -> int:
    """Return the nth Fibonacci number, cached with lru_cache.

    Caching is observable through memoized_fibonacci.cache_info().
    """
    raise NotImplementedError


def spell_dispatcher() -> Callable[[Any], str]:
    """Return a functools.singledispatch spell caster.

    The base implementation handles unknown types; int casts damage,
    str enchants, and list multi-casts.
    """
    raise NotImplementedError


def main() -> None:
    """Demonstrate each functools artifact."""
    raise NotImplementedError


if __name__ == "__main__":
    main()
