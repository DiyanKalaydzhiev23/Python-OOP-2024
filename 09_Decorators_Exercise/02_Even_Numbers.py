def even_parameters(func):
    def wrapper(*args):
        for arg in args:
            if isinstance(arg, int):
                if arg % 2 == 0:
                    continue

            return "Please use only even numbers!"

        return func(*args)

    return wrapper


@even_parameters
def sum_numbers(a, b, c):
    return a + b + c


print(sum_numbers(4, 6, 8))
print(sum_numbers(4, 6, 7))  # Please use only even numbers!
print(sum_numbers(4, 6, 5))
