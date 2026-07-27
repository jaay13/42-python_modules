import sys


def parse_inventory() -> dict[str, int]:
    """Parse sys.argv into an inventory dict, discarding invalid parameters."""

    inventory: dict[str, int] = {}

    # For each argument in argv
    for arg in sys.argv[1:]:
        # split it with delimiter :
        arg_split = arg.split(":")

        # Check 1: Invalid Syntax
        if len(arg_split) != 2:
            print(f"Error - invalid parameter '{arg}'")
            continue

        # unpack name = arg_split[0], quantity = arg_split[1]
        name, quantity = arg_split

        # Check 2: Redundancy in Inventory
        if name in inventory:
            print(f"Redundant item '{name}' - discarding")
            continue

        # Check 3: Quantity values need to be int
        try:
            inventory[name] = int(quantity)
        except ValueError as e:
            print(f"Quantity error for '{name}': {e}")

    return inventory


def main() -> None:
    print("=== Inventory System Analysis ===")

    # Store the created inventory
    inventory = parse_inventory()

    # Check if inventory is empty
    if len(inventory) == 0:
        print(
            "Your inventory is still empty. \n"
            "Gather some items to display stats of your inventory."
        )

    else:
        # A dict prints itself in the {'key': value, ...} format
        print(f"Got inventory: {inventory}")

        # keys() returns a live view, so list() takes a snapshot of the names
        print(f"Item list: {list(inventory.keys())}")

        # len() counts the keys, sum() adds up all the quantities
        total = sum(inventory.values())
        print(
            f"Total quantity of the {len(inventory)} items: "
            f"{total}"
        )

        # Iterating a dict yields its keys, so the value is looked up by name(item)
        for item in inventory:
            quantity = inventory[item]
            percent = quantity / total * 100
            print(f"Item {item} represents {round(percent, 1)}%")

        # Seed both extremes with the first item, which is trivially both
        item_list = list(inventory.keys())
        most_item = item_list[0]
        most_quantity = inventory[most_item]
        least_item = item_list[0]
        least_quantity = inventory[least_item]

        # Two independent if's: an item can be neither the most nor the least.
        # Strict > and < keep the first item on a tie, as dicts stay in
        # insertion order.
        for item in inventory:
            if inventory[item] > most_quantity:
                most_quantity = inventory[item]
                most_item = item
            if inventory[item] < least_quantity:
                least_quantity = inventory[item]
                least_item = item
        print(
            f"Item most abundant: {most_item} with quantity {most_quantity}"
        )
        print(
            f"Item least abundant: {least_item} with quantity {least_quantity}"
        )

        # update() merges a dict in, creating the key when it does not exist
        inventory.update({"golden_apple": 64})
        print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
