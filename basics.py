class Animal():
    def __init__(self):
        self.poop = 1

    def pooping(self):
        print("pooping", self.poop, "poop")


class Duck(Animal):
    def __init__(self):
        super().__init__()
        self.feet = 2

    def walk(self):
        print("walking with", self.feet, "feet")

def print_hello():
    print("hello")

if __name__ == "__main__":
    print("hello")
    animal = Animal()
    duck = Duck()
    duck.pooping()
    duck.walk()
