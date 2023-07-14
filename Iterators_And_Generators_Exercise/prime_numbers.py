from math import sqrt


def get_primes(numbers: list):
    for number in numbers:
        if number <= 1:
            continue

        for divisor in range(2, int(sqrt(number)) + 1):
            if number % divisor == 0:
                break
        else:
            yield number


print(list(get_primes([100_000_007, 2, 4, 3, 5, 6, 9, 1, 0])))
