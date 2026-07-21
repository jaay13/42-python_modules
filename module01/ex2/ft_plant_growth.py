class Plant:
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        growth: float,
    ) -> None:
        self.name = name
        self.hght = height
        self.agey = age
        self.growth_rate = growth
        self.week_growth = 0.0

    def show(self) -> None:
        print(f"{self.name.capitalize()}: ", end="")
        print(f"{round(self.hght, 1)}cm, {self.agey} days old")

    def grow(self) -> None:
        self.hght += self.growth_rate
        self.week_growth += self.growth_rate

    def age(self) -> None:
        self.agey += 1


def main() -> None:
    rose = Plant("rose", 25.0, 30, 0.8)
    print("=== Garden Plant Growth ===")
    for x in range(1, 9):
        rose.show()
        if x != 8:
            print(f"=== Day {x} ===")
            rose.grow()
            rose.age()
    print(f"Growth this week: {round(rose.week_growth, 1)}cm")


if __name__ == "__main__":
    main()
