def garden_operations(operation_number: int) -> None:
    """Trigger a specific error type based on the given operation number."""
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        10 / 0
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        "10" + 10
    else:
        print("Operation completed successfully")


def test_error_types() -> None:
    """Run garden_operations for a range of inputs and catch each error."""
    print("=== Garden Error Types Demo ===")
    for p in range(5):
        print(f"Testing operation {p}...")
        try:
            garden_operations(p)
        except (ValueError, ZeroDivisionError,
                FileNotFoundError, TypeError) as e:
            print(f"Caught {e.__class__.__name__}: {e}")
    print("\nAll error types tested successfully!")


def main() -> None:
    test_error_types()


if __name__ == "__main__":
    main()
