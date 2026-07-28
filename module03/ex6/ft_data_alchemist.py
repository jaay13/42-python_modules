import random

PLAYERS = [
    "Jason", "van", "Benjx", "Nathi", "timmy",
    "Parker", "walker", "luca", "ludmila", "jayjoe"
]


def main() -> None:

    list_capitalized = [name.capitalize() for name in PLAYERS]

    list_only_cap = [name for name in PLAYERS if name == name.capitalize()]

    print("=== Game Data Alchemist ===")

    print(f"\nInitial list of players: {PLAYERS}")

    print(f"\nNew list with all names capitalized: {list_capitalized}")

    print(f"\nNew list of capitalized names only: {list_only_cap}")


    dict_scores = {name: random.randint(0, 1000) for name in list_capitalized}
    print(f"\nScore dict: {dict_scores}")

    total = sum(dict_scores.values())
    num_of_scores = len(dict_scores)
    average = total / num_of_scores
    print(f"Score average is {average}")



    

if __name__ == "__main__":
    main()