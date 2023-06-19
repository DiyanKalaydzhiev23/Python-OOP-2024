from typing import List


def print_list(list_arg):
    for el in list_arg:
        if el is not None:
            print(el)


list1 = [1, 2, None, 3]

print_list(list1)

list2 = [3, 4, 5]

print_list(list2)


a = list("5")

idk_list: List[int, str, float] = [5, "hi my name is", 4.5]
