def shoot(direction):
    r = shooter_pos[0] + directions[direction][0]
    c = shooter_pos[1] + directions[direction][1]
    while 0 <= r < size and 0 <= c < size:
        if matrix[r][c] == "x":
            matrix[r][c] = "."
            return [r, c]
        r += directions[direction][0]
        c += directions[direction][1]


def move(direction, steps):
    r = shooter_pos[0] + directions[direction][0] * steps
    c = shooter_pos[1] + directions[direction][1] * steps
    if not (0 <= r < size and 0 <= c < size):
        return shooter_pos
    if matrix[r][c] == "x":
        return shooter_pos
    else:
        return [r, c]


size = 5
targets_indices = []
all_targets = 0
targets_hit = 0
shooter_pos = []
matrix = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size):
    matrix.append(input().split())
    if "A" in matrix[row]:
        shooter_pos = [row, matrix[row].index("A")]
    all_targets += matrix[row].count("x")

instructions_count = int(input())
for instruction in range(instructions_count):
    command = input().split()
    if command[0] == "shoot":
        direction = command[1]
        targets_down = shoot(direction)
        if targets_down:
            targets_indices.append(targets_down)
            targets_hit += 1
        if targets_hit == all_targets:
            print(f"Training completed! All {all_targets} targets hit.")
            break
    elif command[0] == "move":
        direction = command[1]
        steps = int(command[2])
        shooter_pos = move(direction, steps)

if targets_hit < all_targets:
    print(f"Training not completed! {all_targets - targets_hit} targets left.")

print(*targets_indices, sep="\n")
