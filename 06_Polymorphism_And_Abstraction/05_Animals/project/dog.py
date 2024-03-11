from project.animal import Animal


class Dog(Animal):

    @staticmethod
    def make_sound() -> str:
        return "Woof!"
