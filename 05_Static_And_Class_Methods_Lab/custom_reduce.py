import inspect


def custom_reduce(func, iterable):
    args_count = len(inspect.getfullargspec(func).args)

    accumulator = iterable[0]

    for i in range(1, len(iterable), args_count - 1):
        args_to_pass = iterable[i:i+args_count - 1]  # 3
        accumulator = func(accumulator, *args_to_pass)

    print(accumulator)  # original return


custom_reduce(lambda x, y, z: x * y * z, [2, 3, 4])
