class PizzaDelivery:

    def __init__(self, name: str, price: float, ingredients: dict):
        self.name = name
        self.price = price
        self.ingredients = ingredients  # {cheese: 3, peperoni: 2, olives: 3...}
        self.ordered = False

    def get_ordered_message(self):
        return f"Pizza {self.name} already prepared, and we can't make any changes!"

    def add_extra(self, ingredient: str, quantity: int, price_per_ingredient: float) -> str or None:
        if self.ordered:
            return self.get_ordered_message()

        self.ingredients[ingredient] = self.ingredients.get(ingredient, 0) + quantity
        self.price += quantity * price_per_ingredient

    def remove_ingredient(self, ingredient: str, quantity: int, price_per_ingredient: float) -> str or None:
        if self.ordered:
            return self.get_ordered_message()

        ingredient_quantity = self.ingredients.get(ingredient)

        if not ingredient_quantity:
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"

        if ingredient_quantity < quantity:
            return f"Please check again the desired quantity of {ingredient}!"

        self.ingredients[ingredient] -= quantity
        self.price -= price_per_ingredient * quantity

    def make_order(self) -> str:
        self.ordered = True
        ingredients = ', '.join(f"{k}: {v}" for k, v in self.ingredients.items())
        return f"You've ordered pizza {self.name} prepared with {ingredients} and the price will be {self.price}lv."


margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})
margarita.add_extra('mozzarella', 1, 0.5)
margarita.add_extra('cheese', 1, 1)
margarita.remove_ingredient('cheese', 1, 1)
print(margarita.remove_ingredient('bacon', 1, 2.5))
print(margarita.remove_ingredient('tomatoes', 2, 0.5))
margarita.remove_ingredient('cheese', 2, 1)
print(margarita.make_order())
print(margarita.add_extra('cheese', 1, 1))
