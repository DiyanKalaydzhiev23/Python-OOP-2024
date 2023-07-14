class dictionary_iter:
    def __init__(self, dictionary: dict):
        self.items = list(dictionary.items())
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.items) - 1:
            raise StopIteration

        self.index += 1

        return self.items[self.index]


# second option not working for judge
class dictionary_iterator:
    def __init__(self, dictionary: dict):
        self.items = dictionary.items()

    def __iter__(self):
        return iter(self.items)


result = dictionary_iterator({1: "1", 2: "2"})
for x in result:
    print(x)
