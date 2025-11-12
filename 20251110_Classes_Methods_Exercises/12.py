class Cat:
    def sound(self):
        print("Meow")

class Dog:
    def sound(self):
        print("Woof")


cat = Cat()
dog = Dog()

for animal in (cat, dog):
    animal.sound()
