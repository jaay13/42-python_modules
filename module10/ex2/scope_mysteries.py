"""Memory Depths: closures that remember their creation environment.

State is kept in the enclosing scope with nonlocal - no globals.
"""

from collections.abc import Callable


def mage_counter() -> Callable:
    """Return a function that counts its own calls, starting at 1.

    Two counters created separately keep independent state.
    """
    raise NotImplementedError


def spell_accumulator(initial_power: int) -> Callable:
    """Return a function that adds to a running power total.

    Starts from initial_power and returns the new total each call.
    """
    raise NotImplementedError


def enchantment_factory(enchantment_type: str) -> Callable:
    """Return a function that enchants an item name.

    The returned function formats "enchantment_type item_name",
    e.g. "Flaming Sword".
    """
    raise NotImplementedError


def memory_vault() -> dict[str, Callable]:
    """Return {'store': ..., 'recall': ...} sharing private storage.

    'store' takes (key, value); 'recall' takes (key) and returns the
    value or "Memory not found".
    """
    raise NotImplementedError


def main() -> None:
    """Demonstrate each closure."""
    raise NotImplementedError


if __name__ == "__main__":
    main()
