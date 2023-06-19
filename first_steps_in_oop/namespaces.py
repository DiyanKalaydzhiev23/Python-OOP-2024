def sum(param1):
    return param1


a = sum([1, 2, 3])
print(a)


def f2():
    b = 6
    print(b)


def f1():
    def f1():
        def f1():
            print(3)

        print(2)
        f1()

    print(1)
    f1()


f1()
