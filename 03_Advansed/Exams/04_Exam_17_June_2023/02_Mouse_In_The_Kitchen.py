def new_position_of_mouse(row, col, direction):
    new_r = row + directions[direction][0]
    new_c = col + directions[direction][1]

    return [new_r, new_c]


def check_if_mouse_in_cupboard(row, col, n_c, m_c):
    if row in range(n_c) and col in range(m_c):
        return True
    else:
        return False


def print_final_cupboard(position, matrix):
    row = position[0]
    col = position[1]
    matrix[row][col] = "M"
    for _ in matrix:
        print(*_, sep="")


n, m = [int(x) for x in input().split(",")]  # n = rows, m = columns

mouse_pos = []
cheese_count = 0

directions = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0)
}

cupboard = []
for r in range(n):
    cupboard.append(list(input()))
    if "M" in cupboard[r]:
        mouse_pos = [r, cupboard[r].index("M")]
        cupboard[mouse_pos[0]][mouse_pos[1]] = "*"
    cheese_count += cupboard[r].count("C")
command = input()
while command != "danger":
    current_row = mouse_pos[0]
    current_col = mouse_pos[1]

    new_row, new_col = new_position_of_mouse(current_row, current_col, command)

    if not check_if_mouse_in_cupboard(new_row, new_col, n, m):
        mouse_pos = [new_row - directions[command][0], new_col - directions[command][1]]
        print("No more cheese for tonight!")
        break

    cupboard_element = cupboard[new_row][new_col]

    if cupboard_element == "C":
        cupboard[new_row][new_col] = "*"
        cheese_count -= 1
        mouse_pos = [new_row, new_col]
        if cheese_count == 0:
            print("Happy mouse! All the cheese is eaten, good night!")
            break
    elif cupboard_element == "@":
        mouse_pos = [new_row - directions[command][0], new_col - directions[command][1]]
    elif cupboard_element == "T":
        mouse_pos = [new_row, new_col]
        print("Mouse is trapped!")
        break
    else:
        mouse_pos = [new_row, new_col]

    command = input()

else:
    if cheese_count:
        print("Mouse will come back later!")
print_final_cupboard(mouse_pos, cupboard)
