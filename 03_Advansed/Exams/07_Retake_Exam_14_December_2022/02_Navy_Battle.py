directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}
n = int(input())
battle_field = []
submarine_pos = []
cruisers = 3
submarine_life = 3
for row in range(n):
    battle_field.append(list(input()))
    if "S" in battle_field[row]:
        submarine_pos = [row, battle_field[row].index("S")]
while True:
    direction = input()
    battle_field[submarine_pos[0]][submarine_pos[1]] = "-"
    row = submarine_pos[0] + directions[direction][0]
    col = submarine_pos[1] + directions[direction][1]

    if battle_field[row][col] == "C":
        cruisers -= 1
        battle_field[row][col] = "S"
        if cruisers <= 0:
            print(f"Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
            break
    elif battle_field[row][col] == "*":
        submarine_life -= 1
        battle_field[row][col] = "S"
        if submarine_life <= 0:
            print(f"Mission failed, U-9 disappeared! Last known coordinates [{row}, {col}]!")
            break

    battle_field[row][col] = "S"
    submarine_pos = [row, col]

[print(*row, sep="") for row in battle_field]
