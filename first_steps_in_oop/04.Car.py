class Car:
    def __init__(self, name, model, engine):
        self.name = name
        self.model = model
        self.engine = engine

    def get_info(self):
        return f"This is {self.name} {self.model} with engine {self.engine}"


toyota = Car('toyota', 'supra', '2jz')
nissan = Car('Nissan', 'GT-R', '3.5 V6')

print(toyota.get_info())
print(nissan.get_info())