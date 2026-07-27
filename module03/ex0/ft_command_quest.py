#!/usr/bin/env python3
import sys


def print_argv() -> None:
    """ Print the program name, each command-line argument,
    and the total argument count.
    """

    n = len(sys.argv)
    print("=== Command Quest ===")

    # argv[0] is always the script itself, so it is reported separately
    print(f"Program name: {sys.argv[0]}")

    # Start at index 1 to skip the program name
    if n > 1:
        for i in range(1, n):
            print(f"Argument {i}: {sys.argv[i]}")
    else:
        print("No arguments provided!")

    # Total counts argv[0] as well, hence n and not n - 1
    print(f"Total arguments: {n}")


if __name__ == "__main__":
    print_argv()
