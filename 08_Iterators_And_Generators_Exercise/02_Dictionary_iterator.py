class dictionary_iter:

    def __init__(self, dictionary: dict):  # {1: "1", 2: "2"}
        self.items = list(dictionary.items())  # dictionary.items() => dict_items([(1, "1"), (2, "2")])
        self.index: int = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.items) - 1:
            raise StopIteration

        self.index += 1

        return self.items[self.index]  #  [(1, "1"), (2, "2")][0] => (1, "1")


#  not passing in judge but still correct
class dictionary_iterator:
    def __init__(self, dictionary: dict):  # {1: "1", 2: "2"}
        self.items = dictionary.items() # dictionary.items() => dict_items([(1, "1"), (2, "2")])

    def __iter__(self):
        return iter(self.items)


result = dictionary_iterator({1: "1", 2: "2"})
for x in result:
    print(x)
