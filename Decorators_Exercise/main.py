def type_check(expected_type):
    def decorator(func):
        def wrapper(params):
            return func(params) if type(params) == expected_type else "Bad Type"
        return wrapper
    return decorator


@type_check(str)
def first_letter(word, letter):
    return word[0]

first_letter("a")