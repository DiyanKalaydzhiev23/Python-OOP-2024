from itertools import permutations


def possible_permutations(elements: list):
    for el in permutations(elements):
        yield list(el)


[print(n) for n in possible_permutations([1, 2, 3])]