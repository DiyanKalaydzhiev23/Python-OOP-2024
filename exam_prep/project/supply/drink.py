from project.supply.supply import Supply


class Drink(Supply):
    INITIAL_ENERGY: int = 15

    def __init__(self, name: str):
        super().__init__(name, Drink.INITIAL_ENERGY)

    def details(self) -> str:
        return f"{self.__class__.__name__}: {self.name}, {self.energy}"
