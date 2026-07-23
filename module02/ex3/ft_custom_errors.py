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


def main() -> None:

    print("=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError...")
    try:
        raise PlantError()
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("\nTesting WaterError...")
    try:
        raise WaterError()
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("\nTesting catching all garden errors...")
    try:
        raise PlantError()
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    try:
        raise WaterError()
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    main()
