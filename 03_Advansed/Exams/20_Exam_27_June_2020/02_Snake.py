directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

SIZE = int(input())
matrix = []
snake_pos = []
burrow_pos = []
for r in range(SIZE):
    matrix.append(list(input()))
    if "S" in matrix[r]:
        snake_pos = [r, matrix[r].index("S")]
        matrix[snake_pos[0]][snake_pos[1]] = "."
    elif "B" in matrix[r]:
        burrow_pos.append([r, matrix[r].index("B")])
food_eaten = 0


def check_valid_index(i_r, i_c):
    if i_r in range(SIZE) and i_c in range(SIZE):
        return True
    else:
        return False


while True:
    command = input()
    matrix[snake_pos[0]][snake_pos[1]] = "."
    row = snake_pos[0] + directions[command][0]
    col = snake_pos[1] + directions[command][1]
    if not check_valid_index(row, col):
        print("Game over!")
        break
    if matrix[row][col] == "*":
        food_eaten += 1
        matrix[row][col] = "S"
        snake_pos = [row, col]
        if food_eaten >= 10:
            print(f"You won! You fed the snake.")
            break
    elif matrix[row][col] == "B":
        matrix[row][col] = "."
        burrow_pos.remove([row, col])
        snake_pos = burrow_pos[0]
        row = snake_pos[0]
        col = snake_pos[1]
        matrix[row][col] = "S"
    else:
        matrix[row][col] = "."
        snake_pos = [row, col]

print(f"Food eaten: {food_eaten}")
[print(*row, sep="") for row in matrix]
