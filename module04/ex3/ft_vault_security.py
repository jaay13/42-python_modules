def secure_archive(
        file_name: str, 
        action: str = "read", 
        content: str = ""
) -> tuple[bool, str]:
    """Read or write a file, closed automatically by the with block.

    Returns (success, message): the content on a read, a confirmation
    on a write, or the error reason on failure.
    """
    try:
        if action == "read":
            with open(file_name, "r") as file:
                f_content = file.read()
                return (True, f_content)

        elif action == "write":
            with open(file_name, "w") as file:
                file.write(content)
                return (True, "Content successfully written to file")

        else:
            return (
                False, "Wrong action provided. Use 'write' or 'read' instead."
            )
    except (FileNotFoundError, PermissionError) as e:
        return (False, str(e))


def main() -> None:
    print("=== Cyber Archives Security ===\n")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))

    print()
    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("noperm.txt"))

    print()
    print("Using 'secure_archive' to read from a regular file:")
    # The content read here is what the write call below preserves
    result = secure_archive("test.txt")
    print(result)

    print()
    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive("write.txt", "write", result[1]))


if __name__ == "__main__":
    main()
