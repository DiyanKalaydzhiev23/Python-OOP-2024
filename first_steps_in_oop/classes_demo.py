class Phone:
    def __init__(self, color, size):
        self.color = color
        self.size = size

    def print_color(self):
        print(self.color)


android = Phone("blue", 4.7)
android.ram = 5
print(android.__dict__)

ios = Phone("black", 4)


android_2 = {"color": "blue", "size": 4.7}


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

ivan = Person("ivan", 20)
