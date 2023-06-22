class Shop:
    def __init__(self, name, items):
        self.name = name
        self.items = items

    def get_items_count(self):
        return len(self.items)


shop = Shop("My Shop", ["Apples", "Bananas", "Cucumbers"])
billa = Shop("Billa", ["Billa stuff", "anything"])

print(shop.items)
print(billa.items)
print(shop.get_items_count())
print(billa.get_items_count())
