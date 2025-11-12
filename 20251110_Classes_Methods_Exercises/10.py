
class Vehicle:
    def start(self):
        print("Vehicle start")

class Bike(Vehicle):
    def start(self):
        super().start()
        print("Bike start")

b = Bike()
b.start()
