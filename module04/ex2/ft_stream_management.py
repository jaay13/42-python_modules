from sys import argv, stderr, stdin, stdout


def main() -> None:
    # No arg entered
    if len(argv) == 1:
        print("usage: ft_stream_management.py <file>")
        return

    # Argument(filepath) stored as fd
    fd = argv[1]

    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{fd}'")

    # Opens, reads and prints content from fd unless not correct file
    # given or no permissions to open specified file
    try:
        file = open(fd)
    except (FileNotFoundError, PermissionError) as e:
        # stdout and stderr are buffered separately, so stdout is
        # flushed first to keep both streams in the right order
        stdout.flush()
        print(f"[STDERR] Error opening file '{fd}': {e}", file=stderr)
    else:
        # Whole file put into one string, so the handle can be
        # released before any transforming happens
        content = file.read()

        print("---\n")
        print(content)
        print("---")

        file.close()
        print(f"File '{fd}' closed.")

        # Every newline becomes "#\n", which appends the archive
        # marker to the end of each line
        print("\nTransform data:")
        print("---\n")
        content = content.replace("\n", "#\n")
        print(content)
        print("---")

        # The prompt has no newline of its own, so it must be flushed
        # by hand or it stays in the buffer until something else does
        print("Enter new file name (or empty): ", end="", flush=True)

        # readline() keeps the trailing newline and returns "" at EOF
        # (Ctrl+D), so both cases end up empty after rstrip
        file_name = stdin.readline().rstrip("\n")
        if len(file_name) == 0:
            print("Not saving data.")
            return

        # Announced before the attempt, so it shows on both outcomes
        print(f"Saving data to '{file_name}'")

        # Mode "w" creates the file, or truncates an existing one
        try:
            file = open(file_name, "w")
        except (FileNotFoundError, PermissionError) as e:
            # stdout is drained first, or the buffered line above
            # would arrive after this one when output is redirected
            stdout.flush()
            print(f"[STDERR] Error opening file '{file_name}': {e}",
                  file=stderr)
            print("Data not saved.")
        else:
            # write() takes one str and adds no newline of its own;
            # the "\n" characters are already inside content
            file.write(content)
            print(f"Data saved in file '{file_name}'.")
            file.close()


if __name__ == "__main__":
    main()
