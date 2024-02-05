# calculating the new position of the delivery boy
def new_position(instruction, position):
    row = position[0] + directions[instruction][0]
    col = position[1] + directions[instruction][1]

    return [row, col]


# check if the delivery boy left the neighborhood
def is_in_neighborhood(pos, n, m):
    row = pos[0]
    col = pos[1]
    if row in range(n) and col in range(m):
        return True
    return False


# printing the neighborhood at end of program
def print_results(left, matrix, pos):
    if left:
        matrix[pos[0]][pos[1]] = " "
    else:
        matrix[pos[0]][pos[1]] = "B"
    [print(*data, sep="") for data in matrix]


# collecting neighborhood size
r, c = [int(x) for x in input().split()]

directions = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0)
}

delivery_boy_pos = []
start_pos = []
left_neighborhood = False
neighborhood = []

# collecting neighborhood information
for ro in range(r):
    neighborhood.append(list(input()))

    # get delivery boy location
    if "B" in neighborhood[ro]:
        delivery_boy_pos = [ro, neighborhood[ro].index("B")]
        start_pos = [ro, neighborhood[ro].index("B")]

while True:
    command = input()

    new_delivery_position = new_position(command, delivery_boy_pos)

    if not is_in_neighborhood(new_delivery_position, r, c):
        left_neighborhood = True
        print("The delivery is late. Order is canceled.")
        break

    part_of_neighborhood = neighborhood[new_delivery_position[0]][new_delivery_position[1]]

    if part_of_neighborhood == "*":
        delivery_boy_pos = [new_delivery_position[0] - directions[command][0],
                            new_delivery_position[1] - directions[command][1]]
    elif part_of_neighborhood == "P":
        neighborhood[new_delivery_position[0]][new_delivery_position[1]] = "R"
        delivery_boy_pos = new_delivery_position.copy()
        print("Pizza is collected. 10 minutes for delivery.")
    elif part_of_neighborhood == "A":
        neighborhood[new_delivery_position[0]][new_delivery_position[1]] = "P"
        delivery_boy_pos = new_delivery_position.copy()
        print("Pizza is delivered on time! Next order...")
        break
    else:
        neighborhood[new_delivery_position[0]][new_delivery_position[1]] = "."
        delivery_boy_pos = new_delivery_position.copy()

print_results(left_neighborhood, neighborhood, start_pos)
