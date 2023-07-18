def logged(func):
    def wrapper(*args):
        return f"you called {func.__name__}" \
               f"{args}\n" \
               f"it returned {func(*args)}"

    return wrapper


@logged
def function(*args):
    return 3 + len(args)


print(function(4, 4, 4))

@logged
def sum_func(a, b):
    return a + b


print(sum_func(1, 4))
