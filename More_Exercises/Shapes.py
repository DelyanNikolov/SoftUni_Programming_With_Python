
def pyramid(rows):
    counter = rows
    for steps in range(1, counter + 1):
        print(f"{' ' * counter }{'*' * ((steps * 2) - 1)}")
        counter -= 1


def square(side):
    counter = side
    for steps in range(1, counter + 1):
        print(f"{'*' * 2 * counter}")


def rectangular(side_a, side_b):
    counter = side_a
    for steps in range(1, side_b + 1):
        print(f"{'*' * counter}")


def triangle(side, direction):
    if direction == "up":
        orientation = 1
    else:
        orientation = -1
    counter = side
    for steps in range(1, side + 1):
        print(f"{'*' * counter}")
        counter -= orientation


triangle(5, "s")
