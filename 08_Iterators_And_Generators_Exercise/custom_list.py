class MyListIterator:
    def __init__(self, initial_elements: list):
        self.__initial_elements = initial_elements
        self.__index = 0

    def __next__(self):
        if self.__index >= len(self.__initial_elements):
            raise StopIteration

        value = self.__initial_elements[self.__index]
        self.__index += 1

        return value


class MyList:

    def __init__(self, initial_elements=None):
        # could be a setter
        if not initial_elements:
            self.initial_elements = []
        else:
            self.initial_elements = initial_elements

    def __iter__(self):
        return MyListIterator(self.initial_elements)


my_list = MyList([1, 2, 3])

for el in my_list:
    print(el)

for el in my_list:
    print(el)