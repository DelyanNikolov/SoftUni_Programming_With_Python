from collections import deque


def calculate_new_position(row, col, direction, size):
    directions = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
    }
    new_row = (row + directions[direction][0]) % size
    new_col = (col + directions[direction][1]) % size

    return new_row, new_col


size = 6

rover_pos = None
water_deposit = 0
metal_deposit = 0
concrete_deposit = 0

mars = []
for r in range(size):
    mars.append(input().split())
    if "E" in mars[r]:
        rover_pos = (r, mars[r].index("E"))

commands = deque(input().split(", "))
while commands:
    command = commands.popleft()

    current_row = rover_pos[0]
    current_col = rover_pos[1]

    rover_pos = calculate_new_position(current_row, current_col, command, size)

    element = mars[rover_pos[0]][rover_pos[1]]

    if element == "W":
        water_deposit += 1
        print(f"Water deposit found at {rover_pos}")
    elif element == "M":
        metal_deposit += 1
        print(f"Metal deposit found at {rover_pos}")
    elif element == "C":
        concrete_deposit += 1
        print(f"Concrete deposit found at {rover_pos}")
    elif element == "R":
        print(f"Rover got broken at {rover_pos}")
        break

if water_deposit and  concrete_deposit and metal_deposit:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
