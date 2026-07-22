class Plant:
    class Stats:
        def __init__(self) -> None:
            self._grow_count = 0
            self._age_count = 0
            self._show_count = 0

        def display(self) -> None:
            print(f"Stats: {self._grow_count} grow, ", end="")
            print(f"{self._age_count} age, {self._show_count} show")

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
        self._stats = Plant.Stats()

    @staticmethod
    def check_age(days: int) -> None:
        if days > 365:
            print(f"Is {days} days more than a year? -> True")
        else:
            print(f"Is {days} days more than a year? -> False")

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0, 0.0)

    def show(self) -> None:
        print(f"{self.name.capitalize()}: ", end="")
        print(f"{round(self._height, 1)}cm, {self._agey} days old")
        self._stats._show_count += 1

    def grow(self, days: int = 1) -> None:
        self._height += self.growth_rate * days
        self._stats._grow_count += 1

    def age(self, days: int = 1) -> None:
        self._agey += days
        self._stats._age_count += 1

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
        if not self.blooming:
            print(f" {self.name.capitalize()} has not bloomed yet")
        else:
            print(f" {self.name.capitalize()} is blooming beautifully!")

    def bloom(self) -> None:
        if not self.blooming:
            self.blooming = True


class Seed(Flower):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        growth: float,
        color: str,
    ) -> None:
        super().__init__(name, height, age, growth, color)
        self.seeds = 0

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self.seeds}")

    def bloom(self) -> None:
        super().bloom()
        if self.blooming:
            self.seeds = 42


class Tree(Plant):
    class Stats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade_count = 0

        def display(self) -> None:
            super().display()
            print(f" {self._shade_count} shade")

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
        self._stats: Tree.Stats = Tree.Stats()

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self) -> None:
        print(f"Tree {self.name.capitalize()} now produces a shade ", end="")
        print(f"of {self._height}cm long and {self.trunk_diameter}cm wide.")
        self._stats._shade_count += 1


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

    def grow(self, days: int = 1) -> None:
        super().grow(days)
        self.nutritional_value += days


def display_stats(plant: Plant) -> None:
    print(f"[statistics for {plant.name.capitalize()}]")
    plant._stats.display()


def main() -> None:

    flower = Flower("rose", 15.0, 10, 0.8, "red")
    tree = Tree("oak", 200.0, 365, 0.2, 5.0)
    seed = Seed("sunflower", 80.0, 45, 1.5, "yellow")
    anon = Plant.anonymous()

    print("=== Garden statistics ===")

    print("=== Check year-old")
    Plant.check_age(30)
    Plant.check_age(400)

    print()
    print("=== Flower")
    flower.show()

    display_stats(flower)

    print(f"[asking the {flower.name} to grow and bloom]")
    flower.grow(10)
    flower.bloom()

    flower.show()

    display_stats(flower)

    print()
    print("=== Tree")
    tree.show()

    display_stats(tree)

    print(f"[asking the {tree.name} to produce shade]")
    tree.produce_shade()

    display_stats(tree)

    print()
    print("=== Seed")
    seed.show()

    print(f"[make {seed.name} grow, age and bloom]")
    seed.grow(20)
    seed.age(20)
    seed.bloom()

    seed.show()

    display_stats(seed)

    print()
    print("=== Anonymous")
    anon.show()

    display_stats(anon)


if __name__ == "__main__":
    main()
