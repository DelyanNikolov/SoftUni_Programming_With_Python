def check_all_collected():
    if not decorations_count and not gifts_count and not cookies_count:
        return True
    return False


def move_santa(position, direction, steps, matrix, r, c):
    global decorations_count, cookies_count, gifts_count, number_of_gifts, number_of_cookies, number_of_decoration
    directions = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
    }
    new_row = None
    new_col = None
    new_santa_pos = position
    for step in range(int(steps)):
        row = new_santa_pos[0]
        col = new_santa_pos[1]

        matrix[row][col] = "x"

        new_row = (row + directions[direction][0]) % r
        new_col = (col + directions[direction][1]) % c
        if matrix[new_row][new_col] == "D":
            decorations_count -= 1
            number_of_decoration += 1
        elif matrix[new_row][new_col] == "G":
            gifts_count -= 1
            number_of_gifts += 1
        elif matrix[new_row][new_col] == "C":
            cookies_count -= 1
            number_of_cookies += 1
        matrix[new_row][new_col] = "Y"
        new_santa_pos = new_row, new_col
        if check_all_collected():
            break
    return new_row, new_col


rows, cols = [int(x) for x in input().split(", ")]

santa_pos = None
decorations_count = 0
gifts_count = 0
cookies_count = 0

number_of_decoration = 0
number_of_gifts = 0
number_of_cookies = 0

workshop = []
for r in range(rows):
    workshop.append(input().split())
    if "Y" in workshop[r]:
        santa_pos = r, workshop[r].index("Y")
    if "D" in workshop[r]:
        decorations_count += workshop[r].count("D")
    if "G" in workshop[r]:
        gifts_count += workshop[r].count("G")
    if "C" in workshop[r]:
        cookies_count += workshop[r].count("C")


command = input()
while not command == "End":
    direction, steps = command.split("-")
    santa_pos = move_santa(santa_pos, direction, steps, workshop, rows, cols)
    if check_all_collected():
        break
    command = input()

if not decorations_count and not gifts_count and not cookies_count:
    print("Merry Christmas!")
print("You've collected:")
print(f"- {number_of_decoration} Christmas decorations")
print(f"- {number_of_gifts} Gifts")
print(f"- {number_of_cookies} Cookies")

for row_info in workshop:
    print(*row_info, sep=" ")