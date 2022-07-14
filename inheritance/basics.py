class Animal():
    def __init__(self):
        self.poop = 1

    def pooping(self):
        print("pooping", self.poop, "poop")

class Material():
    def __init__(self):
        self.element = "iron"

    def check_iron(self):
        print("I have %d iron" % (1))

class Duck(Animal, Material):
    def __init__(self):
        # super().__init__() also ok
        super(Duck, self).__init__() # super will only refer to the first class in the multiple class inheritance (i.e. Animal)
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
    duck.check_iron() # However, the method will get inherited
