def print_rhombus(n):
    print_top_rhombus_part(n)
    print_bottom_rhombus_part(n)


def print_top_rhombus_part(n):
    for star in range(1, n + 1):
        print(f"{' ' * (n - star)}{'* ' * star}")


def print_bottom_rhombus_part(n):
    for star in range(n - 1, 0, -1):
        print(f"{' ' * (n - star)}{'* ' * star}")


n = int(input())
print_rhombus(n)
