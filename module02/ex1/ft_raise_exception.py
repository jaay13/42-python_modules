def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    if temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    return temp


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

    try:
        print("\nInput data is '100'")
        input_temperature("100")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    else:
        print("Temperature is now 100°C")

    try:
        print("\nInput data is '-50'")
        input_temperature("-50")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    else:
        print("Temperature is now -50°C")
    finally:
        print("\nAll tests completed - program didn't crash!")


def main() -> None:
    print("=== Garden Temperature ===")
    test_temperature()


if __name__ == "__main__":
    main()
