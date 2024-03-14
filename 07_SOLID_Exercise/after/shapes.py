from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def calculate_area(self):
        ...


class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class Triangle(Shape):

    def __init__(self, base: int, height: int):
        self.base = base
        self.height = height

    def calculate_area(self):
        return self.base * self.height / 2


class Square(Shape):

    def __init__(self, side: int):
        self.side = side

    def calculate_area(self):
        return self.side * self.side


class AreaCalculator:

    def __init__(self, shapes: list):
        self.shapes = shapes

    @property
    def shapes(self):
        return self.__shapes

    @shapes.setter
    def shapes(self, value):
        if not isinstance(value, list):
            raise AssertionError("Must be a list!")

        self.__shapes = value

    @property
    def total_area(self):
        total = 0

        for shape in self.shapes:
            total += shape.calculate_area()

        return total


shapes = [Rectangle(2, 3), Rectangle(1, 6), Triangle(1, 12), Square(3)]
calculator = AreaCalculator(shapes)
print("The total area is:", calculator.total_area)
