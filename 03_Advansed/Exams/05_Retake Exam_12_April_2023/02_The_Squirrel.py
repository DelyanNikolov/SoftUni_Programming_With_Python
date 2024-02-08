def next_move(direction, position):
    row, col = position[0], position[1]
    row = row + directions[direction][0]
    col = col + directions[direction][1]
    return [row, col]


def chek_if_squirrel_left(position):
    row = position[0]
    col = position[1]
    if row in range(SIZE) and col in range(SIZE):
        return False
    return True


def is_collected_nuts_enough(count):
    if count >= 3:
        return True
    return False


SIZE = int(input())
commands = input().split(", ")

squirrel_pos = []
collected_nuts = 0

directions = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0)
}
field = []
for r in range(SIZE):
    field.append(list(input()))
    if "s" in field[r]:
        squirrel_pos = [r, field[r].index("s")]

for command in commands:

    new_pos = next_move(command, squirrel_pos)

    if chek_if_squirrel_left(new_pos):
        print("The squirrel is out of the field.")
        break

    step_element = field[new_pos[0]][new_pos[1]]

    if step_element == "t":
        print("Unfortunately, the squirrel stepped on a trap...")
        break

    elif step_element == "h":
        collected_nuts += 1
        field[new_pos[0]][new_pos[1]] = "*"
        if is_collected_nuts_enough(collected_nuts):
            print("Good job! You have collected all hazelnuts!")
            break

    elif step_element == "*":
        pass

    squirrel_pos = [new_pos[0], new_pos[1]]
else:
    print("There are more hazelnuts to collect.")
print(f"Hazelnuts collected: {collected_nuts}")
