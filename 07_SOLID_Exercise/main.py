from abc import ABC, abstractmethod

class Car(ABC):
    pass

class Fuel(ABC):

    @abstractmethod
    def refuel(self):
        ...

class Charge(ABC):

    @abstractmethod
    def charge(self):
        ...

class CarWithCombustionEngine(Car, Fuel):

    def refuel(self):
        print("Fueling with A95")


class ElectricCar(Car, Charge):

    def charge(self):
        print("Charging as your iphone")