import random

ACHIEVEMENTS = [
    'Taking Inventory', 'Getting Wood', 'Benchmaking',
    'Time to Mine!', 'Hot Topic', 'Acquire Hardware',
    'Time to Farm!', 'Bake Bread', 'The Lie',
    'Getting an Upgrade', 'Delicious Fish', 'On A Rail',
    'Time to Strike!', 'Monster Hunter', 'Cow Tipper',
    'When Pigs Fly', 'Sniper Duel', 'DIAMONDS!',
    'We Need to Go Deeper', 'Return to Sender', 'Into Fire',
    'Local Brewery', 'The End?', 'Free the End', 'Enchanter',
    'Overkill', 'Librarian', 'Adventuring Time', 'The Beginning?',
    'The Beginning.', 'Beaconator', 'Repopulation',
    'Diamonds to you!', 'Overpowered'
]


def gen_player_achievements() -> set[str]:
    """Return a set of randomly chosen achievements for one player."""

    k = random.randint(4, 10)
    achievements_sample = set(random.sample(ACHIEVEMENTS, k))
    return achievements_sample


def main() -> None:
    print("=== Achievement Tracker System ===\n")

    PLAYERS = ["Jason", "Van", "Benjx", "Dylan", "Alice"]
    players = {name: gen_player_achievements() for name in PLAYERS}

    # Printing each Player with their Achievements
    for name, achievements in players.items():
        print(f"Player {name}: {achievements}")

    # List of all distinct Achievements from all Players
    achievements_distinct = set().union(*players.values())
    print(f"\nAll distinct achievements: {achievements_distinct}")

    # Common Achievements of all Players
    achievements_common = achievements_distinct.intersection(*players.values())
    print(f"\nCommon achievements: {achievements_common}\n")

    # Exclusive Achievements per Player
    for name, achievements in players.items():
        others: set[str] = set()
        for other, s in players.items():
            if other != name:
                others = others.union(s)
        exclusive = achievements.difference(others)
        print(f"Only {name} has: {exclusive}")

    # Missing Achievements against Master List of Achievements per Player
    for name, achievements in players.items():
        missing = set(ACHIEVEMENTS).difference(achievements)
        print(f"\n{name} is missing: {missing}")


if __name__ == "__main__":
    main()
