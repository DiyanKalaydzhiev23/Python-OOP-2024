from project.animal import Animal


class Cat(Animal):

    @staticmethod
    def make_sound() -> str:
        return "Meow meow!"
