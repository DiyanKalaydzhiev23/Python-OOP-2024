from project.animal import Animal


class Cat(Animal):
    def make_sound(self) -> str:
        return "Meow meow!"
