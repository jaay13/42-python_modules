def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:

    print("\nInput data is '25'")
    try:
        input_temperature("25")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    else:
        print("Temperature is now 25°C")

    print("\nInput data is 'abc'")
    try:
        input_temperature("abc")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    else:
        print("Temperature is now 25°C")

    print("\nAll tests completed - program didn't crash!")


def main() -> None:
    print("=== Garden Temperature ===")
    test_temperature()


if __name__ == "__main__":
    main()
