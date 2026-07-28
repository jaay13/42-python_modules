import random

PLAYERS = [
    "Jason", "van", "Benjx", "Nathi", "timmy",
    "Parker", "walker", "luca", "ludmila", "jayjoe"
]


def main() -> None:
    # Normalize every name to Title Case, regardless of its original form
    list_capitalized = [name.capitalize() for name in PLAYERS]

    # Keep only the names that were already capitalized in the original list
    list_only_cap = [name for name in PLAYERS if name == name.capitalize()]

    print("=== Game Data Alchemist ===")

    print(f"\nInitial list of players: {PLAYERS}")

    print(f"\nNew list with all names capitalized: {list_capitalized}")

    print(f"\nNew list of capitalized names only: {list_only_cap}")

    # Assign each capitalized name a random score between 0 and 1000
    dict_scores = {name: random.randint(0, 1000) for name in list_capitalized}
    print(f"\nScore dict: {dict_scores}")

    # len() counts the keys, sum() adds up all the scores
    total = sum(dict_scores.values())
    num_of_scores = len(dict_scores)
    average = total / num_of_scores
    print(f"Score average is {round(average, 2)}")

    # items() hands back (key, value) pairs directly, no lookup needed
    high_scores = {
        name: score for name, score in dict_scores.items() if score > average
    }
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
