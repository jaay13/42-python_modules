import sys


def ft_score_analytics() -> None:
    """Parse score arguments and print player score analytics."""

    print("=== Player Score Analytics ===")

    # Keep only the arguments that convert to int, reporting the others
    score_list = []
    for arg in sys.argv[1:]:
        try:
            score_list += [int(arg)]
        except ValueError:
            print(f"Invalid parameter: '{arg}'")

    # Stats need at least two scores to be meaningful
    players = len(score_list)
    if players == 1:
        print("Sorry mate but you'll have to provide more than one score :(")
    elif players > 1:
        # Range is the spread between the best and the worst score
        score_total = sum(score_list)
        score_average = score_total / players
        score_max = max(score_list)
        score_min = min(score_list)
        score_range = score_max - score_min
        print(f"Scores processed: {score_list}")
        print(f"Total players: {players}")
        print(f"Total score: {score_total}")
        print(f"Average score: {score_average}")
        print(f"High score: {score_max}")
        print(f"Low score: {score_min}")
        print(f"Score range: {score_range}")
    else:
        print(
            "No scores provided. Usage: python3 ft_score_analytics.py "
            "<score1> <score1> ..."
        )


if __name__ == "__main__":
    ft_score_analytics()
