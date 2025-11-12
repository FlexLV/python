
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
