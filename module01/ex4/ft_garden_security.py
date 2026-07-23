class Plant:
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        growth: float,
    ) -> None:
        self.name = name
        self._height = height if height >= 0 else 0.0
        self._agey = age if age >= 0 else 0
        self.growth_rate = growth

    def show(self) -> None:
        print(f"{self.name.capitalize()}: ", end="")
        print(f"{round(self._height, 1)}cm, {self._agey} days old")

    def grow(self) -> None:
        self._height += self.growth_rate

    def age(self) -> None:
        self._agey += 1

    def set_height(self, height: int) -> None:
        if height >= 0:
            self._height = height + 0.0
            print(f"Height updated: {height}cm")
        else:
            print(f"{self.name.capitalize()}: Error, height can't be negative")
            print("Height update rejected")

    def get_height(self) -> float:
        return self._height

    def set_age(self, age: int) -> None:
        if age >= 0:
            self._agey = age
            print(f"Age updated: {age} days")
        else:
            print(f"{self.name.capitalize()}: Error, age can't be negative")
            print("Age update rejected")

    def get_age(self) -> int:
        return self._agey


def main() -> None:
    plant = Plant("dandelion", 11.0, 14, 0.9)

    print("=== Garden Security System ===")
    print("Plant created: ", end="")
    plant.show()

    print()
    plant.set_height(22)
    plant.set_age(28)

    print()
    plant.set_height(-22)
    plant.set_age(-28)

    print()
    print("Current state: ", end="")
    plant.show()


if __name__ == "__main__":
    main()
