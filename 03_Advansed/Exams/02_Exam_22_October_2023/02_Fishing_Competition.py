def new_ship_position(old_pos, direction, size):
    row = old_pos[0] + directions[direction][0]
    col = old_pos[1] + directions[direction][1]
    pos = [row, col]
    new_coordinates = []
    for coordinate in pos:
        if coordinate < 0:
            coordinate = size - 1
        elif coordinate > size - 1:
            coordinate = 0
        new_coordinates.append(coordinate)
    return new_coordinates


directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

ship_pos = []
fish_amount = 0
ship_sunk = False

size = int(input())

fishing_area = []
# crating the matrix
for r in range(size):
    fishing_area.append(list(input()))
    # locating the ship position and storing the coordinates
    if "S" in fishing_area[r]:
        ship_pos = [r, fishing_area[r].index("S")]

command = input()
while command != "collect the nets":

    # calculating new ship position
    fishing_area[ship_pos[0]][ship_pos[1]] = "-"
    new_pos = new_ship_position(ship_pos, command, size)
    current_element = str(fishing_area[new_pos[0]][new_pos[1]])
    fishing_area[new_pos[0]][new_pos[1]] = "S"
    if current_element == "W":
        ship_pos = new_pos
        ship_sunk = True
        fish_amount = 0
        break
    elif current_element.isdigit():
        fish_amount += int(current_element)
    ship_pos = new_pos

    command = input()

if ship_sunk:
    print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. "
          f"Last coordinates of the ship: [{ship_pos[0]},{ship_pos[1]}]")
    exit()
if fish_amount >= 20 and not ship_sunk:
    print(f"Success! You managed to reach the quota!")
else:
    print(f"You didn't catch enough fish and didn't reach the quota! "
          f"You need {20 - fish_amount} tons of fish more.")

if fish_amount and not ship_sunk:
    print(f"Amount of fish caught: {fish_amount} tons.")
if not ship_sunk:
    [print(*row, sep="") for row in fishing_area]
