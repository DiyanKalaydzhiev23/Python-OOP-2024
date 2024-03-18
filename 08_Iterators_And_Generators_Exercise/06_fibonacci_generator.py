def fibonacci():
    n1, n2 = 0, 1

    while True:
        yield n1
        n1, n2 = n2, n1 + n2

generator = fibonacci()

for _ in range(50):
    print(next(generator))
