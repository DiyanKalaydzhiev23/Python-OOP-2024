class sequence_repeat:
    def __init__(self, sequence: str, number: int):
        self.sequence = sequence
        self.number = number
        self.idx = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx == self.number - 1:
            raise StopIteration

        self.idx += 1

        return self.sequence[self.idx % len(self.sequence)]


for el in sequence_repeat('ab', 5):
    print(el)


my_iter = sequence_repeat('ab', 5).__iter__()

while True:
    try:
        element = next(my_iter)
        print(element)
    except StopIteration:
        break