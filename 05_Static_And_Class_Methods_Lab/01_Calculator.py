from functools import reduce


class Calculator:

    @staticmethod
    def add(*nums) -> int:
        return sum(nums)

    @staticmethod
    def multiply(*nums) -> int:
        return reduce(lambda x, y: x * y, nums)

    @staticmethod
    def subtract(*nums) -> int:
        return reduce(lambda x, y: x - y, nums)

    @staticmethod
    def divide(*nums) -> float:
        return reduce(lambda x, y: x / y, nums)

