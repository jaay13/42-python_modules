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


class WaterError(GardenError):
    """Raised when an issue occurs with watering."""

    def __init__(
            self, error_message: str = "Not enough water in the tank!"
    ) -> None:
        super().__init__(error_message)


def water_plant(plant_name: str) -> None:
    """ """
    try:
        if plant_name == plant_name.capitalize():
            print("[OK]")

        else:
            raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    except PlantError as e:
        print(f"Caught PlantError: {e}")


def test_watering_system() -> None:
    """ """
    print("Opening watering system")
    try:
        water_plant("Dahlia")
    except PlantError as e:
        print(
            f"Caught PlantError: {e}"
            f".. ending tests and returning to main"
        )
    finally:
        print("Closing watering system")


def main() -> None:
    print("=== Garden Watering System ===")

    print("\nTesting valid plants...")
    test_watering_system()

if __name__ == "__main__":
    main()
