def even_numbers(function):
    def wrapper(numbers):
        return [n for n in function(numbers) if n % 2 == 0]

    return wrapper


@even_numbers
def get_numbers(numbers):
    return numbers


print(get_numbers([1, 2, 3, 4, 5]))
