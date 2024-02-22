directions = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
    }

size = int(input())

jet_fighter_pos = []
jet_armor = 300
enemies_count = 0

airspace = []
for row in range(size):
    airspace.append(list(input()))
    if "J" in airspace[row]:
        jet_fighter_pos = [row, airspace[row].index("J")]
    if "E" in airspace[row]:
        enemies_count += airspace[row].count("E")

while True:
    command = input()

    current_row = jet_fighter_pos[0]
    current_col = jet_fighter_pos[1]

    airspace[current_row][current_col] = "-"

    next_row = current_row + directions[command][0]
    next_col = current_col + directions[command][1]

    element = airspace[next_row][next_col]

    airspace[next_row][next_col] = "J"

    if element == "E":
        enemies_count -= 1
        if enemies_count == 0:
            print("Mission accomplished, you neutralized the aerial threat!")
            break
        else:
            jet_armor -= 100
            if jet_armor <= 0:
                print(f"Mission failed, your jetfighter was shot down! Last coordinates [{next_row}, {next_col}]!")
                break
            else:
                airspace[next_row][next_col] = "-"
                jet_fighter_pos = [next_row, next_col]
    elif element == "R":
        jet_armor = 300
        airspace[next_row][next_col] = "-"
        jet_fighter_pos = [next_row, next_col]
    elif element == "-":
        jet_fighter_pos = [next_row, next_col]

[print(*r, sep="") for r in airspace]
