class Vehicle:
    def __init__(self, mileage: float, max_speed: int=150, fuel_capacity: float=56):
        self.mileage = mileage
        self.max_speed = max_speed
        self.gadgets = []


car = Vehicle(20)

print(car.max_speed)
print(car.mileage)
print(car.gadgets)

car.gadgets.append('Hudly Wireless')
print(car.gadgets)
