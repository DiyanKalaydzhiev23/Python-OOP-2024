class Flower:

    def __init__(self, name: str, water_requirements: int):
        self.name = name
        self.water_requirements = water_requirements
        self.is_happy = False

    def water(self, quantity: int) -> None:
        if quantity >= self.water_requirements:
            self.is_happy = True

    def status(self) -> str:
        return f"{self.name} is {'' if self.is_happy else 'not '}happy"
        # if self.is_happy:
        #     return f"{self.name} is happy"
        #
        # return f"{self.name} is not happy"


flower = Flower("Lilly", 100)
flower.water(100)
print(flower.status())

tulip = Flower("John", 50)
tulip.water(200)
print(tulip.status())
