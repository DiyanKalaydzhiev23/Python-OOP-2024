class MyList:
    def __init__(self, my_list):
        self.my_list = my_list
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.my_list) - 1:
            raise StopIteration

        self.index += 1

        return self.my_list[self.index]


for el in MyList([1, 2, 3]):
    print(el)


def number_multiplied_by_two(numbers):
    for num in numbers:
        yield num * 2


my_generator = number_multiplied_by_two([1, 2, 3])

print(next(my_generator))
print(next(my_generator))
