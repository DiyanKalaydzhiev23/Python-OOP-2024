from time import time


def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()

        print(end - start)

        return result

    return wrapper


@measure_time
def sum_numbers_to(to_number):
    result = 0

    for num in range(to_number):
        result += num

    return result


sum_numbers_to(1000000)