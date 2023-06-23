class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def set_x(self, new_x: int):
        self.x = new_x

    def set_y(self, new_y: int):
        self.y = new_y

    def __str__(self):
        return f"The point has coordinates ({self.x},{self.y})"


p = Point(3, 4)
print(p)

p.set_x(5)
p.set_y(6)

print(p)