class Plant:
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        growth: float,
    ) -> None:
        self.name = name
        self._hght = height if height >= 0 else 0.0
        self._agey = age if age >= 0 else 0
        self.growth_rate = growth
        self.week_growth = 0.0

    def show(self) -> None:
        print(f"{self.name.capitalize()}: ", end="")
        print(f"{round(self._hght, 1)}cm, {self._agey} days old")

    def grow(self) -> None:
        self._hght += self.growth_rate
        self.week_growth += self.growth_rate

    def age(self) -> None:
        self._agey += 1

    def set_height(self, height: int) -> None:
        if height >= 0:
            self._hght = height + 0.0
            print(f"Height updated: {height}cm")
        else:
            print(f"{self.name.capitalize()}: Error, height can't be negative")
            print("Height update rejected")

    def get_height(self) -> float:
        return self._hght

    def set_age(self, age: int) -> None:
        if age >= 0:
            self._agey = age
            print(f"Age updated: {age} days")
        else:
            print(f"{self.name.capitalize()}: Error, age can't be negative")
            print("Age update rejected")

    def get_age(self) -> int:
        return self._agey


class Flower(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        growth: float,
        color: str,
    ) -> None:
        super().__init__(name, height, age, growth)
        self.color = color
        self.blooming = False

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self.blooming is False:
            print(f" {self.name.capitalize()} has not bloomed yet")
        else:
            print(f" {self.name.capitalize()} is blooming beautifully!")

    def bloom(self) -> None:
        if self.blooming is False:
            print(f"[asking the {self.name} to bloom]")
            self.blooming = True
        else:
            pass


class Tree(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        growth: float,
        trunk_diameter: float,
    ) -> None:
        super().__init__(name, height, age, growth)
        self.trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self) -> None:
        print(f"[asking the {self.name} to produce shade]")
        print(f"Tree {self.name.capitalize()} now produces a shade ", end="")
        print(f"of {self._hght}cm long and {self.trunk_diameter}cm wide.")


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        growth: float,
        harvest_season: str,
        nutritional_value: int,
    ) -> None:
        super().__init__(name, height, age, growth)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season.capitalize()}")
        print(f" Nutritional value: {self.nutritional_value}")

    def grow(self) -> None:
        super().grow()
        self.nutritional_value += 1


def main() -> None:

    flower = Flower("rose", 15.0, 10, 0.8, "red")
    tree = Tree("oak", 200.0, 365, 0.2, 5.0)
    vegetable = Vegetable("tomato", 5.0, 10, 2.1, "april", 0)

    print("=== Garden Plant Types ===")
    print("=== Flower")
    flower.show()
    flower.bloom()
    flower.show()
    flower.bloom()

    print()
    print("=== Tree")
    tree.show()
    tree.produce_shade()

    print()
    print("=== Vegetable")
    vegetable.show()
    print(f"[make {vegetable.name} grow and age for 20 days]")
    for x in range(20):
        vegetable.grow()
        vegetable.age()
    vegetable.show()


if __name__ == "__main__":
    main()
