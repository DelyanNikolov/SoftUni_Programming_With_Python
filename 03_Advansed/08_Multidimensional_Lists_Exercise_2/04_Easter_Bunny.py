size = int(input())

field = []
bunny_position = []
best_path = []
best_direction = None
max_collected_eggs = float("-inf")

for row in range(size):
    field.append(input().split())
    if "B" in field[row]:
        bunny_position = [row, field[row].index("B")]

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for direction, position in directions.items():
    row, col = bunny_position[0] + position[0], bunny_position[1] + position[1]
    eggs_collected = 0
    path = []

    while 0 <= row < size and 0 <= col < size:
        if field[row][col] == "X":
            break
        eggs_collected += int(field[row][col])
        path.append([row, col])
        row, col = row + position[0], col + position[1]

    if eggs_collected >= max_collected_eggs:
        max_collected_eggs = eggs_collected
        best_path = path
        best_direction = direction

print(best_direction)
print(*best_path, sep="\n")
print(max_collected_eggs)
