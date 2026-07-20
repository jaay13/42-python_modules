
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

def main():
    rose = Plant("rose", 15.0, 10, 0.8)

    print("=== Garden Security System ===")
    print(f"Plant created: ", end='')
    rose.show()

    print()
    rose.set_height(25)
    rose.set_age(30)

    print()
    rose.set_height(-25)
    rose.set_age(-30)

    print()
    print(f"Current state: ", end='')
    rose.show()

if __name__ == "__main__":
    main()