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


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')
