def type_check(expected_type):
    def decorator(func):
        def wrapper(*args):
            for arg in args:
                if not isinstance(arg, expected_type):
                    return "Bad Type"

            return func(*args)

        return wrapper

    return decorator


@type_check(int)
def sum_numbers(a, b):
    return a + b

print(sum_numbers(5, 6.5))