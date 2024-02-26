class Car:
    TIRES = 4

    def __init__(self, hp: int):
        self.hp = hp

    def __str__(self):
        return f"This is car with {self.hp} hp"

    def __repr__(self):
        return f"This is car with {self.hp} hp"


nissan = Car(255)
toyota = Car(320)

Car.TIRES = 5

print(nissan.TIRES)
print(toyota.TIRES)