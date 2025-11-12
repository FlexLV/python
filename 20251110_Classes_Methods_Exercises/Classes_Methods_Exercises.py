# All code uplodaed to github https://github.com/FlexLV/python/tree/main/20251110_Classes_Methods_Exercises
# All exercises done by Group

# 1 Exercise

class Person:
    def greet(self):
        print("Hello!")

a = Person()
a.greet()


# 2 Exercise

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

a = Person("Ernests", 20)
a.display()

# 3 Exercise

class Person:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

a = Person("Ernests", 20)

a.display()


# 4 Exercise

class Person:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Employee(Person):
    def __init__(self, name, age=18, job_role="Unknown"):
        super().__init__(name, age)
        self.job_role = job_role

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Job Role:", self.job_role)



a = Employee("Ernests", 20, "DevOps Engineer")


a.display()


# 5 Exercise

class Address:
    def __init__(self, fname, lname, email):
        self.fname = fname
        self.lname = lname
        self.email = email

    def display(self):
        print("First Name:", self.fname)
        print("Last Name:", self.lname)
        print("Email:", self.email)

a = Address("Ernests", "Dejus", "ernests@gmail.com")
a.display()

# 6 Exercise

class AddressBook:
    def __init__(self):
        self.addresses = []

    def add_address(self, name, address):
        entry = {"name": name, "address": address}
        self.addresses.append(entry)
        print(f"Added address for {name}.")

    def find_address(self, name):
        for entry in self.addresses:
            if entry["name"].lower() == name.lower():
                return entry["address"]
        return "Address not found."

book = AddressBook()
book.add_address("Ernests", "Mettern Strase, Deggendorf")
book.add_address("Aleksis", "Dieter-Görlitz-Platz, Deggendorf")

print(book.find_address("Ernests"))
print(book.find_address("Aleksis"))

# 7 Exercise

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds")

a = BankAccount(400)
a.deposit(200)
a.withdraw(100)

# 8 Exercise

class Car:
    wheels = 4

car1 = Car()
car2 = Car()

print(car1.wheels)
print(car2.wheels)

# 9 Exercise

class Vehicle:
    def start(self):
        print("Vehicle start")

class Bike(Vehicle):
    def start(self):
        print("Bike start")

v = Vehicle()
b = Bike()

v.start()
b.start()

# 10 Exercise

class Vehicle:
    def start(self):
        print("Vehicle start")

class Bike(Vehicle):
    def start(self):
        super().start()
        print("Bike start")

b = Bike()
b.start()

# 11 Exercise

class Student:
    def __init__(self):
        self.__grade = None

    def set_grade(self, grade):
        self.__grade = grade

    def get_grade(self):
        return self.__grade

s = Student()
s.set_grade(95)
print(s.get_grade())

# 12 Exercise
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

# 13 Exercise

class Note:
    def __init__(self, filename):
        self.filename = filename

    def write_note(self, text):
        with open(self.filename, "a") as file:
            file.write(text + "\n")
        print("Note added")

    def read_note(self):
        with open(self.filename, "r") as file:
            contents = file.read()
        print("File content :\n" + contents)

n = Note("note.txt")
n.write_note("Texts")
n.read_note()

# 14 Exercise


from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    def start(self):
        print("Car is starting")

    def stop(self):
        print("Car has stopped")


class Bicycle(Vehicle):
    def start(self):
        print("Bicycle is starting")

    def stop(self):
        print("Bicycle has stopped")

car = Car()
bike = Bicycle()

car.start()
car.stop()
bike.start()
bike.stop()
