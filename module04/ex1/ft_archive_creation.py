from sys import argv


def main() -> None:
    # No arg entered
    if len(argv) == 1:
        print("Usage: ft_archive_creation.py <file>")
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
        print(f"Error opening file '{fd}': {e}")
    else:
        # Whole file put into one string, so the handle can be
        # released before any transforming happens. finally runs even
        # if read() raises, so the handle is never left open
        try:
            content = file.read()
        finally:
            file.close()

        print("---\n")
        print(content)
        print("---")

        print(f"File '{fd}' closed.")

        # Every newline becomes "#\n", which appends the archive
        # marker to the end of each line
        print("\nTransform data:")
        print("---\n")
        content = content.replace("\n", "#\n")
        print(content)
        print("---")

        # Empty input means the user declined to save, and a closed
        # stdin (EOFError, e.g. Ctrl+D) is treated the same way
        try:
            file_name = input("Enter new file name (or empty): ")
        except EOFError:
            print("Not saving data.")
            return
        if len(file_name) == 0:
            print("Not saving data.")
            return

        # Mode "w" creates the file, or truncates an existing one
        try:
            file = open(file_name, "w")
        except (FileNotFoundError, PermissionError) as e:
            print(f"Error opening file '{file_name}': {e}")
        else:
            print(f"Saving data to '{file_name}'")

            # write() takes one str and adds no newline of its own;
            # the "\n" characters are already inside content. close()
            # is in finally, so a failed write still frees the handle
            try:
                file.write(content)
            finally:
                file.close()

            print(f"Data saved in file '{file_name}'.")


if __name__ == "__main__":
    main()
