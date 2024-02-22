from enum import Enum


class Color(Enum, object):
    RED = 1
    GREEN = 2
    BLUE = 3


color = Color.RED
print(color.name, color.value)
