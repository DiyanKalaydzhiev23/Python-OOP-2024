class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step  # 2
        self.count = count  # 6
        self.iterations = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.iterations == self.count - 1:
            raise StopIteration

        self.iterations += 1

        return self.iterations * self.step


numbers = take_skip(2, 6)
for number in numbers:
    print(number)
