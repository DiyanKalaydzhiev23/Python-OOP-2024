from project.product import Product


class Food(Product):
    DEFAULT_QUANTITY = 15

    def __init__(self, name: str):
        super().__init__(name, self.DEFAULT_QUANTITY)
