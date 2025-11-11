
class Person:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

p1 = Person("Ernests", 20)

p1.display()

