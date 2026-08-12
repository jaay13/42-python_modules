"""Lambda Sanctum: transform magical data with anonymous functions.

Every transformation here must be written as a lambda - no named
helper functions for the simple operations.
"""


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    """Sort artifacts by 'power', strongest first.

    Each artifact is {'name': str, 'power': int, 'type': str}.
    Uses sorted() with a lambda key.
    """
    return sorted(
        artifacts, key=lambda artifact: artifact["power"], reverse=True
        )


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    """Keep only mages whose 'power' is at least min_power.

    Each mage is {'name': str, 'power': int, 'element': str}.
    Uses filter() with a lambda predicate.
    """
    return list(filter(lambda mage: mage["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    """Wrap each spell name as "* name *".

    Uses map() with a lambda.
    """
    return list(map(lambda spell: f"* {spell} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    """Summarise the power levels of a list of mages.

    Returns {'max_power': int, 'min_power': int, 'avg_power': float},
    with avg_power rounded to 2 decimals. Uses max() and min() with
    lambda keys. An empty list yields zeros, since max() and min()
    raise on an empty sequence.
    """
    if not mages:
        return {"max_power": 0, "min_power": 0, "avg_power": 0.0}

    max_power = max(mages, key=lambda mage: mage["power"])["power"]
    min_power = min(mages, key=lambda mage: mage["power"])["power"]
    powers = map(lambda mage: mage["power"], mages)
    avg_power = round(sum(powers) / len(mages), 2)

    return {
        "max_power": max_power,
        "min_power": min_power,
        "avg_power": avg_power,
    }


def main() -> None:
    """Demonstrate each spell on sample data."""

    artifacts = [{'name': 'Light Prism', 'power': 108, 'type': 'accessory'},
                 {'name': 'Storm Crown', 'power': 82, 'type': 'relic'},
                 {'name': 'Lightning Rod', 'power': 117, 'type': 'armor'},
                 {'name': 'Lightning Rod', 'power': 100, 'type': 'weapon'}]

    mages = [{'name': 'Jordan', 'power': 56, 'element': 'light'},
             {'name': 'Casey', 'power': 98, 'element': 'ice'},
             {'name': 'River', 'power': 54, 'element': 'lightning'},
             {'name': 'Riley', 'power': 94, 'element': 'wind'},
             {'name': 'Jordan', 'power': 83, 'element': 'light'}]

    spells = ['shield', 'flash', 'fireball', 'heal']

    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    first, second = sorted_artifacts[0], sorted_artifacts[1]
    print(f"{first['name']} ({first['power']} power) comes before "
          f"{second['name']} ({second['power']} power)\n")

    print("Testing spell transformer...")
    print(" ".join(spell_transformer(spells)))

    print("\nTesting power filter...")
    print("Only mages with more or equal than 70 power:")
    above_70 = power_filter(mages, 70)
    print(", ".join(
        map(lambda mage: f"{mage['name']} ({mage['power']})", above_70))
    )

    print("\nTesting mage stats...")
    stats = mage_stats(mages)
    print(
        f"Max Power: {stats['max_power']}, "
        f"Min Power: {stats['min_power']}, "
        f"Average(rounded): {stats['avg_power']}"
    )


if __name__ == "__main__":
    main()
