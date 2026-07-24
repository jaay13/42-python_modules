class GardenError(Exception):
    """Base exception for all garden-related errors."""

    def __init__(
        self, error_message: str = "Unknown Garden error!"
    ) -> None:
        super().__init__(error_message)
        self.error_message = error_message


class PlantError(GardenError):
    """Raised when an issue occurs with a plant."""

    def __init__(
            self, error_message: str = "Unknown Plant error!"
    ) -> None:
        super().__init__(error_message)


class WaterError(GardenError):
    """Raised when an issue occurs with watering."""

    def __init__(
            self, error_message: str = "Unknown Water error!"
    ) -> None:
        super().__init__(error_message)


def main() -> None:

    print("=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("\nTesting WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("\nTesting catching all garden errors...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    main()
