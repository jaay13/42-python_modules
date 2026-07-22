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

    def show(self) -> None:
        print(f"{self.name.capitalize()}: ", end="")
        print(f"{round(self.hght, 1)}cm, {self.agey} days old")

    def grow(self) -> None:
        self.hght += self.growth_rate

    def age(self) -> None:
        self.agey += 1


def main() -> None:
    plants = [
        Plant("rose", 25.0, 30, 0.8),
        Plant("oak", 200.0, 365, 0.2),
        Plant("pink tulip", 12.5, 40, 1.1),
        Plant("cactus", 15.0, 120, 0.15),
        Plant("tomato", 33.0, 144, 2.1),
    ]
    print("=== Plant Factory Output ===")
    for p in plants:
        print("Created: ", end="")
        p.show()


if __name__ == "__main__":
    main()
