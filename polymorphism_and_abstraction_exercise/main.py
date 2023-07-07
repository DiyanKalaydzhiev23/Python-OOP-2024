from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    @abstractmethod
    def work(self):
        ...


class Employee(Person):

    def work(self):
        print("working...")


class Boss(Person):

    def work(self):
        print("taking risks")


ivan = Employee("ivan", 22)
pesho = Boss("pesho", 34)

ivan.work()
pesho.work()