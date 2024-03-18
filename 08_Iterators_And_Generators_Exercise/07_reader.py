def read_next(*args):
    for seq in args:
        # Option 1
        # for el in seq:
        #     yield el

        # Option 2
        yield from seq


for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
    print(item, end='')
