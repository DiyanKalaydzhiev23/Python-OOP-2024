class Car:
    ENGINE = "combustion"

    def __init__(self, name, model):
        self.name = name
        self.model = model


nissan = Car("nissan", "GT-R")
ford = Car("ford", "Focus RS")

print(Car.ENGINE, nissan.ENGINE)

Car.ENGINE = "electric"

print(Car.ENGINE, ford.ENGINE)

a = filter(lambda n: n > 0, [1, 2, 3])
