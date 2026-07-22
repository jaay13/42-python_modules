def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        try:
            int("abc")
        except ValueError as e:
            print(f"Caught ValueError: {e}")
    elif operation_number == 1:
        try:
            10 / 0
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
    elif operation_number == 2:
        try:
            open("/non/existent/file")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
    elif operation_number == 3:
        try:
            "12" + 10
        except TypeError as e:
            print(f"Caught: TypeError {e}")
    else:
        try:
            int(10)
        finally:
            print("Operation completed successfully")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    try:
        for p in range(5):
            print(f"Testing operation {p}...")
            garden_operations(p)
            
    finally:
        print("\nAll error types tested successfully!")


def main() -> None:
    test_error_types()


if __name__ == "__main__":
    main()
