def read_next(*args):
    for item in args:
        for element in item:
            yield element

    # Option 2
    # yield from item


for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
    print(item, end='')
