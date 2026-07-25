#!/usr/bin/env python3
import sys


def print_argv() -> None:
    """ Print the program name, each command-line argument,
    and the total argument count.
    """

    n = len(sys.argv)
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    if n > 1:
        for i in range(1, n):
            print(f"Argument {i}: {sys.argv[i]}")
    else:
        print("No arguments provided!")
    print(f"Total arguments: {n}")


if __name__ == "__main__":
    print_argv()
