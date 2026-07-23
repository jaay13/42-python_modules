def input_temperature(temp_str: str) -> int:
    """Convert and validate a temperature string.

    Raises ValueError if out of range.
    """
    temp = int(temp_str)
    if temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    if temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    return temp


def test_temperature() -> None:
    """Test input_temperature with valid, invalid and boundary values."""

    # Valid input, within range
    print("\nInput data is '25'")
    try:
        input_temperature("25")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    else:
        print("Temperature is now 25°C")

    # Invalid input, not a number
    print("\nInput data is 'abc'")
    try:
        input_temperature("abc")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")

    # Invalid input, above max threshold
    print("\nInput data is '100'")
    try:
        input_temperature("100")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")

    # Invalid input, below min threshold
    print("\nInput data is '-50'")
    try:
        input_temperature("-50")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")

    print("\nAll tests completed - program didn't crash!")


def main() -> None:
    print("=== Garden Temperature ===")
    test_temperature()


if __name__ == "__main__":
    main()
