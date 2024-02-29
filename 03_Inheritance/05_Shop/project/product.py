class Product:

    def __init__(self, name: str, quantity: int):
        self.name = name
        self.quantity = quantity

    def increase(self, quantity: int) -> None:
        self.quantity += quantity

    def decrease(self, quantity: int) -> None:
        if quantity <= self.quantity:
            self.quantity -= quantity

    def __repr__(self):
        return self.name
