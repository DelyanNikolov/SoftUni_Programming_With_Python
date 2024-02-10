def get_element_of_db(position, direct, db):
    global cursor_pos
    directions = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1),
    }
    element_row = position[0] + directions[direct][0]
    element_col = position[1] + directions[direct][1]

    cursor_pos = (element_row, element_col)

    return db[element_row][element_col]


size = 6

data_base = []
for r in range(size):
    data_base.append(input().split())

cursor_pos = eval(input())


while True:
    command = input().split(", ")
    if command[0] == "Stop":
        break
    elif command[0] == "Create":
        direction = command[1]
        value = command[2]
        element = get_element_of_db(cursor_pos, direction, data_base)
        if element == ".":
            data_base[cursor_pos[0]][cursor_pos[1]] = value
        else:
            continue

    elif command[0] == "Update":
        direction = command[1]
        value = command[2]
        element = get_element_of_db(cursor_pos, direction, data_base)
        if element == ".":
            continue
        else:
            data_base[cursor_pos[0]][cursor_pos[1]] = value

    elif command[0] == "Delete":
        direction = command[1]
        element = get_element_of_db(cursor_pos, direction, data_base)
        if element == ".":
            continue
        else:
            data_base[cursor_pos[0]][cursor_pos[1]] = "."
    elif command[0] == "Read":
        direction = command[1]
        element = get_element_of_db(cursor_pos, direction, data_base)
        if element == ".":
            continue
        else:
            print(element)

for row in data_base:
    print(*row, sep=" ")
