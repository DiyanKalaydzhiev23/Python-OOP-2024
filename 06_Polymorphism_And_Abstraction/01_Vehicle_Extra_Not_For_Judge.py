from abc import ABC, abstractmethod


class Vehicle(ABC):  # Abstract Base Class
    def __init__(self, fuel_quantity: float, fuel_consumption: float):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @property
    @abstractmethod
    def conditioner_on(self) -> float:
        ...

    def drive(self, distance: float) -> None:
        consumption = (self.conditioner_on + self.fuel_consumption) * distance

        if self.fuel_quantity >= consumption:
            self.fuel_quantity -= consumption

    @abstractmethod
    def refuel(self, fuel: float) -> None:
        pass


class Car(Vehicle):

    @property
    def conditioner_on(self) -> float:
        return 0.9

    def refuel(self, fuel: float) -> None:
        self.fuel_quantity += fuel


class Truck(Vehicle):
    TANK_PERCENTAGE_FILL: float = 0.95

    @property
    def conditioner_on(self) -> float:
        return 1.6

    def refuel(self, fuel: float) -> None:
        self.fuel_quantity += fuel * self.TANK_PERCENTAGE_FILL
