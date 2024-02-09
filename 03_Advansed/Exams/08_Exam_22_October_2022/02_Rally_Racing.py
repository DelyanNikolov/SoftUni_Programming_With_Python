directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

size = int(input())
car_number = input()

tunnel_positions = []
car_pos = (0, 0)
distance_traveled = 0

race_track = []
for r in range(size):
    race_track.append(list(input().split()))
    if "T" in race_track[r]:
        tunnel_positions.append((r, race_track[r].index("T")))

command = input()
while command != "End":
    new_row = car_pos[0] + directions[command][0]
    new_col = car_pos[1] + directions[command][1]

    element = race_track[new_row][new_col]

    if element == "T":
        current_tunnel = (new_row, new_col)
        race_track[new_row][new_col] = "."
        tunnel_positions.remove(current_tunnel)
        car_pos = tunnel_positions[0]
        race_track[car_pos[0]][car_pos[1]] = "."
        distance_traveled += 30
    elif element == "F":
        print(f"Racing car {car_number} finished the stage!")
        distance_traveled += 10
        car_pos = (new_row, new_col)
        break
    else:
        distance_traveled += 10
        car_pos = (new_row, new_col)

    command = input()
else:
    print(f"Racing car {car_number} DNF.")

print(f"Distance covered {distance_traveled} km.")

race_track[car_pos[0]][car_pos[1]] = "C"
for row in race_track:
    print(*row, sep="")
