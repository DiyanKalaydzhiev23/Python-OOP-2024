class countdown_iterator:

    def __init__(self, count: int):
        self.count = count + 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count <= 0:
            raise StopIteration

        self.count -= 1

        return self.count


iterator = countdown_iterator(10)

for el in iterator:
    print(el)

for el in iterator:
    print(el)