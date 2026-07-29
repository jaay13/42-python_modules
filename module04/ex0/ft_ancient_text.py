from sys import argv


def main() -> None:
    # No arg entered
    if len(argv) == 1:
        print("usage: ft_anchient_text.py <file>")
        return

    # Argument(filepath) stored as fd
    fd = argv[1]

    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{fd}'")

    # Opens, reads and prints content from fd unless not correct file
    # given or no permissions to open specified file
    try:
        file = open(fd)
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error opening file {fd}: {e}")
    else:
        content = file.read()
        print("---\n\n")
        print(content)
        print("\n\n---")
        print(f"File '{fd}' closed.")


if __name__ == "__main__":
    main()
