
class Plant:
    def __init__(self, name, height, age, growth_rate):
        self.name = name
        self.heighty = height
        self.agey = age
        self.growth_rate = growth_rate
        self.week_growth = 0

    def show(self):
        print(f"{self.name.capitalize()}: {round(self.heighty, 1)}cm, {self.agey} days old")
           
    def grow(self):
        self.heighty += self.growth_rate
        self.week_growth += self.growth_rate

    def age(self):
        self.agey += 1

def main():
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