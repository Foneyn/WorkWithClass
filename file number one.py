class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        print(f"{self.name} is eating.")

class Bird(Animal):
    def __init__(self, name, age, species):
        super().__init__(name, age)
        self.species = species

    def make_sound(self):
        print(f"{self.name} the {self.species} chirps.")

class Mammal(Animal):
    def __init__(self, name, age, species):
        super().__init__(name, age)
        self.species = species

    def make_sound(self):
        print(f"{self.name} the {self.species} makes a mammal sound.")

class Reptile(Animal):
    def __init__(self, name, age, species):
        super().__init__(name, age)
        self.species = species

    def make_sound(self):
        print(f"{self.name} the {self.species} hisses.")

def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_staff(self, staff):
        self.staff.append(staff)

class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        print(f"{self.name} is feeding {animal.name}.")

class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        print(f"{self.name} is healing {animal.name}.")

# Пример использования классов
bird1 = Bird("Sparrow", 2, "Sparrow")
mammal1 = Mammal("Tiger", 5, "Tiger")
reptile1 = Reptile("Snake", 3, "Snake")

zookeeper = ZooKeeper("John")
veterinarian = Veterinarian("Alice")

zoo = Zoo()
zoo.add_animal(bird1)
zoo.add_animal(mammal1)
zoo.add_animal(reptile1)
zoo.add_staff(zookeeper)
zoo.add_staff(veterinarian)

animal_sound(zoo.animals)
zookeeper.feed_animal(bird1)
veterinarian.heal_animal(mammal1)