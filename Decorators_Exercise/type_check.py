def type_check(expected_type):
    def decorator(func):
        def wrapper(*args):
            for arg in args:
                if not isinstance(arg, expected_type):
                    return "Bad Type"

            return func(*args)

        return wrapper

    return decorator


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('4'))
print(first_letter(['Not', 'A', 'String']))
