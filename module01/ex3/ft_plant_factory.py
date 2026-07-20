
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
    plants = [
        Plant("rose", 25.0, 30, 0.8),
        Plant("oak", 200.0, 365, 0.2),
        Plant("pink Tulip", 12.5, 40, 1.1),
        Plant("cactus", 15.0, 120, 0.15),
        Plant("tomato", 33.0, 144, 2.1)
    ]
    print("=== Plant Factory Output ===")
    for p in plants:
        print(f"Created: ", end='') 
        p.show()

if __name__ == "__main__":
    main()