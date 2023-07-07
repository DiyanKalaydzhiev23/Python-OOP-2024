from project.animal import Animal


class Dog(Animal):
    def make_sound(self) -> str:
        return "Woof!"
