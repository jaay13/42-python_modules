def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    try:
        print("\nInput data is '25'")
        input_temperature("25")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    else:
        print("Temperature is now 25°C")

    try:
        print("\nInput data is 'abc'")
        input_temperature("abc")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    else:
        print("Temperature is now 25°C")
    finally:
        print("\nAll tests completed - program didn't crash!")


def main() -> None:
    print("=== Garden Temperature ===")
    test_temperature()


if __name__ == "__main__":
    main()
