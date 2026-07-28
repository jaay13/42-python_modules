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

    # sys.argv always holds at least the program name, so n == 1 means
    # no arguments were passed
    if n == 1:
        print("No arguments provided!")
    else:
        i = 1
        for arg in sys.argv[1:]:
            print(f"Argument {i}: {arg}")
            i += 1

    # Total counts argv[0] as well, hence n and not n - 1
    print(f"Total arguments: {n}")


if __name__ == "__main__":
    print_argv()
