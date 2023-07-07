from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, fuel_capacity: float, fuel_consumption: float):
        self.fuel_quantity = fuel_capacity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance: float) -> None:
        ...

    @abstractmethod
    def refuel(self, fuel: float) -> None:
        ...


class Car(Vehicle):
    CONDITIONER_ON = 0.9

    def drive(self, distance: float) -> None:
        consumption = (self.fuel_consumption + Car.CONDITIONER_ON) * distance

        if self.fuel_quantity >= consumption:
            self.fuel_quantity -= consumption

    def refuel(self, fuel: float) -> None:
        self.fuel_quantity += fuel


class Truck(Vehicle):
    CONDITIONER_ON = 1.6
    TANK_PERCENTAGE_FILL = 0.95

    def drive(self, distance: float) -> None:
        consumption = (self.fuel_consumption + Truck.CONDITIONER_ON) * distance

        if self.fuel_quantity >= consumption:
            self.fuel_quantity -= consumption

    def refuel(self, fuel: float) -> None:
        self.fuel_quantity += fuel * Truck.TANK_PERCENTAGE_FILL


truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)