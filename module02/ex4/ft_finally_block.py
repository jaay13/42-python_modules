class GardenError(Exception):
    """Base exception for all garden-related errors."""

    def __init__(
        self, error_message: str = "Unknown Garden error"
    ) -> None:
        super().__init__(error_message)
        self.error_message = error_message


class PlantError(GardenError):
    """Raised when an issue occurs with a plant."""

    def __init__(
            self, error_message: str = "The tomato plant is wilting!"
    ) -> None:
        super().__init__(error_message)


def water_plant(plant_name: str) -> None:
    """Water plant_name if capitalized, else raise PlantError."""

    if plant_name == plant_name.capitalize():
        print(f"Watering {plant_name}: [OK]")

    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def test_watering_system() -> None:
    """Run valid then invalid watering cycles, always closing via finally."""

    print("\nTesting valid plants...")

    try:
        print("Opening watering system")
        water_plant("Dahlia")
        water_plant("Sweet potatos")
        water_plant("Sugercane")

    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
        return

    finally:
        print("Closing watering system")

    print("\nTesting invalid plants...")

    try:
        print("Opening watering system")
        water_plant("Tomato")
        water_plant("lettuce")

    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
        return

    finally:
        print("Closing watering system")
        print("\nCleanup always happens, even with errors!")


def main() -> None:
    print("=== Garden Watering System ===")
    test_watering_system()


if __name__ == "__main__":
    main()
