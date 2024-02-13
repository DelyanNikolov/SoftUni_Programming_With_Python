player_pos = []
touched_opponents_count = 0
turns_count = 0

directions = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0)
}

n, m = [int(x) for x in input().split()]

playground = []
for r in range(n):
    playground.append(input().split())
    if "B" in playground[r]:
        player_pos = [r, playground[r].index("B")]
        playground[r][playground[r].index("B")] = "-"
while True:
    command = input()
    if command == "Finish":
        break

    current_row = player_pos[0]
    current_col = player_pos[1]

    desired_row = current_row + directions[command][0]
    desired_col = current_col + directions[command][1]

    if not (0 <= desired_row < n and 0 <= desired_col < m):
        continue

    elif playground[desired_row][desired_col] == "O":
        continue

    element = playground[desired_row][desired_col]

    if element == "P":
        touched_opponents_count += 1
        player_pos = [desired_row, desired_col]
        playground[player_pos[0]][player_pos[1]] = "-"
        turns_count += 1
        if touched_opponents_count == 3:
            break
    elif element == "-":
        turns_count += 1
        player_pos = [desired_row, desired_col]

print(f"Game over!")
print(f"Touched opponents: {touched_opponents_count} Moves made: {turns_count}")
