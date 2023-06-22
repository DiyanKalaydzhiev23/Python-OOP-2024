from typing import List, Callable


def hello():
    return [], ()


class Shop:
    def __init__(self, name, items: List[str]):
        self.name = name
        self.items = items


shop = Shop("My Shop", ["Apples", "Bananas", "Cucumbers"])
billa = Shop("Billa", ["Billa stuff", "anything"])

print(shop.items)
print(billa.items)
print(hello())
# print(shop.get_items_count())


products = ["apples", "bananas", "oranges"]
filtered_products = filter(lambda x: True == True, products)

print(next(filtered_products))
print(next(filtered_products))
print(next(filtered_products))
print(next(filtered_products))