class Dog:
    def __init__(self,name):
        self.name=name

    def sond(self):
        print(f"{self.name} makes the sound : Woof!")

class Cat:
    def __init__(self, name):
        self.name = name

    def sond(self):
        print(f"{self.name} makes the sound : Meow!")

class Bird:
    def __init__(self, name):
        self.name = name

    def sond(self):
        print(f"{self.name} makes the sound : Cherp!")



dog = Dog("Buddy")
cat = Cat("Mack")
bird = Bird("Tweetie")



for animal in (dog,cat,bird):
    animal.sond()