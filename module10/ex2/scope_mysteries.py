"""Memory Depths: closures that remember their creation environment.

State is kept in the enclosing scope with nonlocal - no globals.

In Python, the nonlocal keyword lets you declare a variable in a

nested function as not local to that function. It allows you to

modify variables defined in the enclosing scope from within an inner

function.
"""

from collections.abc import Callable


def mage_counter() -> Callable:
    """Return a function that counts its own calls, starting at 1.

    Two counters created separately keep independent state.
    """
    count = 0

    def counter() -> int:
        # When I assign to count in this scope,
        # target the enclosing function's variable, not a new local one.
        nonlocal count
        count += 1  # count = count + 1 (would create a new count in scope)
        return count

    return counter


def spell_accumulator(initial_power: int) -> Callable:
    """Return a function that adds to a running power total.

    Starts from initial_power and returns the new total each call.
    """
    init = initial_power

    def accumulator(amount: int) -> int:
        nonlocal init
        init += amount
        return init

    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    """Return a function that enchants an item name.

    The returned function formats "enchantment_type item_name",
    e.g. "Flaming Sword". No nonlocal needed: enchantment_type is
    only read here, never reassigned.
    """

    def enchanter(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"

    return enchanter


def memory_vault() -> dict[str, Callable]:
    """Return {'store': ..., 'recall': ...} sharing private storage.

    'store' takes (key, value); 'recall' takes (key) and returns the
    value or "Memory not found".
    """
    storage = {}

    def store(key: str, value: object) -> None:
        # No nonlocal: mutates the dict storage points to,
        # doesn't rebind the name storage itself.
        storage[key] = value

    def recall(key: str) -> object:
        return storage.get(key, "Memory not found")

    return {"store": store, "recall": recall}


def main() -> None:
    """Demonstrate each closure."""

    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()

    print("counter_a call:", counter_a())
    print("counter_a call:", counter_a())
    print("counter_b call:", counter_b())
    print("\nCalling counter_b 5 times more")
    for _ in range(2, 7):
        print(f"counter_b call: {counter_b()}")

    print("\nTesting spell accumulator...")
    accumulator = spell_accumulator(100)
    print(f"Base 100, add 28: {accumulator(28)}")
    print(f"Base 100, add 128: {accumulator(128)}")
    print(f"Base 100, add 256: {accumulator(256)}")

    print("\nTesting enchantment factory...")
    print(enchantment_factory("Sharpness V:")("Diamond Sword"))
    print(enchantment_factory("Loyalty III:")("Trident"))
    print(enchantment_factory("Efficiency V:")("Netherite Pickaxe"))

    print("\nTesting memory vault...")
    vault = memory_vault()
    print("Store 'secret' = 42")
    vault["store"]("secret", 42)
    print(f"Recall 'secret': {vault['recall']('secret')}")
    print(f"Recall 'unknown': {vault['recall']('unknown')}")
    print("Store 'unknown' = Wither Skeleton Skull")
    vault["store"]("unknown", "Wither Skeleton Skull")
    print(f"Recall 'unknown': {vault['recall']('unknown')}")


if __name__ == "__main__":
    main()
