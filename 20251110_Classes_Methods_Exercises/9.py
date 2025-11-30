
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
