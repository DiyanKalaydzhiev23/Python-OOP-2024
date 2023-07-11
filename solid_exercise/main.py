import copy

a = [[1], [2], [3]]
b = a.copy()

b[0].append(4)
print(a)


def copy(old_list):
    new_list = []

    for el in old_list:
        new_list.append(el)

    return new_list