def cache(func):
    def wrapper(num):
        if not wrapper.log.get(num):  # 0(1)
            wrapper.log[num] = func(num)

        return wrapper.log[num]

    wrapper.log = {}

    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(3)
fibonacci(3)
print(fibonacci.log)
