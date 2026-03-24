class Animal:
    def __init__(self,name):
        self.name=name

    def sound(self):
        print("some generic animal sound")

    def description(self):
        print(f"This is an animal name {self.name}")

class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        print("Woof!Woof!")

    def description(self):
        super().description()

        print(f"Breed: {self.breed}")


class cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def sound(self):
        print("meow!Meow!")

    def description(self):
        super().description()
        print(f"color: {self.color}")

animal = Animal("generic animal")

animal.sound()
animal.description()

dog = Dog("Bella", "Rottweiler")
dog.sound()
dog.description()

cat = Cat("Nimo", "white")
cat.sound()
cat.description()