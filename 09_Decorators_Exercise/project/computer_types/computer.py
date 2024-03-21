from abc import ABC, abstractmethod
from typing import Dict
from math import log2


class Computer(ABC):
    ONE_BLOCK_OF_RAM_PRICE: int = 100

    def __init__(self, manufacturer: str, model: str):
        self.manufacturer = manufacturer
        self.model = model
        self.processor = None
        self.ram = None
        self.price = 0

    @property
    @abstractmethod
    def type(self) -> str:
        ...

    @property
    @abstractmethod
    def available_processors(self) -> Dict[str, int]:
        ...

    @property
    @abstractmethod
    def max_ram(self) -> int:
        ...

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        if not value.strip():
            raise ValueError("Manufacturer name cannot be empty.")

        self.__manufacturer = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if not value.strip():
            raise ValueError("Model name cannot be empty.")

        self.__model = value

    @staticmethod
    def power_of_two(ram: int):
        result = log2(ram)  # log of ram with base 2 = 2^x = ram; result is x
        return result.is_integer()

    def configure_computer(self, processor: str, ram: int) -> str:
        if processor not in self.available_processors:
            raise ValueError(f"{processor} is not compatible with {self.type} {self.manufacturer} {self.model}!")

        if ram > self.max_ram or not self.power_of_two(ram):
            raise ValueError(f"{ram}GB RAM is not compatible with {self.type} {self.manufacturer} {self.model}!")

        self.set_parts(processor, ram)

        return f"Created {self.__repr__()} for {self.price}$."

    def set_parts(self, processor: str, ram: int) -> None:
        self.processor = processor
        self.ram = ram
        self.price += self.available_processors[processor]  # processor AMD Ryzen 7 => 500$
        self.price += int(log2(ram)) * self.ONE_BLOCK_OF_RAM_PRICE

    def __repr__(self):
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"
