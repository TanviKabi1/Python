from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Bike(Vehicle):
    def start(self):
        print("Bike starts with a key")

class ElectricCar(Vehicle):
    def start(self):
        print("Electric car starts with a button")

vehicles = [Bike(), ElectricCar()]

for vehicle in vehicles:
    vehicle.start()
