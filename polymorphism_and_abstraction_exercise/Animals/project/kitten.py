from project.cat import Cat


class Kitten(Cat):

    def __init__(self, name: str, age: int):
        super().__init__(name, age, "Female")

    def make_sound(self) -> str:
        return "Meow"
