class Plant:
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        growth: float,
    ) -> None:
        self.name = name
        self.height = height
        self.agey = age
        self.growth_rate = growth
        self.week_growth = 0.0

    def show(self) -> None:
        print(f"{self.name.capitalize()}: ", end="")
        print(f"{round(self.height, 1)}cm, {self.agey} days old")

    def grow(self) -> None:
        self.height += self.growth_rate
        self.week_growth += self.growth_rate

    def age(self) -> None:
        self.agey += 1


def main() -> None:
    plant = Plant("dahlia", 12.0, 10, 0.6)
    print("=== Garden Plant Growth ===")
    for x in range(1, 9):
        plant.show()
        if x != 8:
            print(f"=== Day {x} ===")
            plant.grow()
            plant.age()
    print(f"Growth this week: {round(plant.week_growth, 1)}cm")


if __name__ == "__main__":
    main()
