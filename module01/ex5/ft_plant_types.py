
class Plant:
    def __init__(self, name, height, age, growth_rate):
        self.name = name
        self._heighty = height if height >= 0 else 0.0
        self._agey = age if age >= 0 else 0
        self.growth_rate = growth_rate
        self.week_growth = 0

    def show(self):
        print(f"{self.name.capitalize()}: {round(self._heighty, 1)}cm, {self._agey} days old")
           
    def grow(self):
        self._heighty += self.growth_rate
        self.week_growth += self.growth_rate

    def age(self):
        self._agey += 1
    
    def set_height(self, height):
        if height >= 0:
            self._heighty = height
            print(f"Height updated: {self._heighty}cm")
        else:
            print(f"{self.name.capitalize()}: Error, height can't be negative\nHeight update rejected")
    
    def get_height(self):
        return self._heighty

    def set_age(self, age):
        if age >= 0:
            self._agey = age
            print(f"Age updated: {self._agey} days")
        else:
            print(f"{self.name.capitalize()}: Error, age can't be negative\nAge update rejected")
    
    def get_age(self):
        return self._agey

class Flower(Plant):
    def __init__(self, name, height, age, growth_rate, color):
        super().__init__(name, height, age, growth_rate) 
        self.color = color
        self.blooming = 0

    def show(self):
        super().show()
        print(f" Color: {self.color}")
    
    def bloom(self):
        if self.blooming == 0:
            print(f" {self.name.capitalize()} has not bloomed yet")
            print(f"[asking the {self.name} to bloom]")
            self.blooming += 1
        else:
            print(f" {self.name.capitalize()} is blooming beautifully!")

class Tree(Plant):
    def __init__(self, name, height, age, growth_rate, trunk_diameter):
        super().__init__(name, height, age, growth_rate)
        self.trunk_diameter = trunk_diameter
    
    def show(self):
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self):
        print(f"[asking the {self.name} to produce shade]")
        print(f"Tree {self.name.capitalize()} now produces a shade of {self._heighty}cm long and {self.trunk_diameter}cm wide.")

class Vegetable(Plant):
    def __init__(self, name, height, age, growth_rate, harvest_season, nutritional_value):
        super().__init__(name, height, age, growth_rate)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
    
    def show(self):
        super().show()
        print(f" Harvest season: {self.harvest_season.capitalize()}")
        print(f" Nutritional value: {self.nutritional_value}")
        if self.nutritional_value == 0:
            print(f"[make {self.name} grow and age for 20 days]")

    def grow(self):
        super().grow()
        self.nutritional_value += 1
    
    # def age(self):
    #     super().age()
    #     self.nutritional_value += 0.5

def main():

    rose = Flower("rose", 15.0, 10, 0.8, "red")
    oak = Tree("oak", 200.0, 365, 0.2, 5.0)
    tomato = Vegetable("tomato", 5.0, 10, 2.1, "april", 0)

    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose.show()
    rose.bloom()
    rose.show()
    rose.bloom()

    print()
    print("=== Tree")
    oak.show()
    oak.produce_shade()

    print()
    print("=== Vegetable")
    tomato.show()
    for x in range (20):
        tomato.grow()
        tomato.age()
    tomato.show()

if __name__ == "__main__":
    main()