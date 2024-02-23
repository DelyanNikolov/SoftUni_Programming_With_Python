def print_triangle(n):
    top_part(n)
    bottom_part(n)


def top_part(n):
    for row in range(1, n + 1):
        for num in range(1, row + 1):
            print(num, end=" ")
        print()


def bottom_part(n):
    for row in range(n, 0, -1):
        for num in range(1, row):
            print(num, end=" ")
        print()


print_triangle(20)
