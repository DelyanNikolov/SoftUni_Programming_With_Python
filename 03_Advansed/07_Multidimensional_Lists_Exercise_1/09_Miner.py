from collections import deque


def collecting_field_info(field):
    """traversing the matrix and collecting coordinates for: coal, end of route, miner start position"""
    for row in range(n):
        for col in range(n):
            if field[row][col] == "c":
                current_coordinates = (row, col)
                coal_coordinates.append(current_coordinates)
            elif field[row][col] == "e":
                current_coordinates = (row, col)
                end_of_route.append(current_coordinates)
            elif field[row][col] == "s":
                current_coordinates = (row, col)
                start_position.append(current_coordinates)


def moving_miner(actions):
    command = moving_commands.popleft()
    current_x, current_y = start_position[0]
    x, y = commands[command]
    new_x, new_y = current_x + x, current_y + y
    new_position = (new_x, new_y)
    if 0 <= new_x < n and 0 <= new_y < n:
        if new_position in coal_coordinates:
            coal_coordinates.remove(new_position)
            matrix[new_x][new_y] = "*"
        elif new_position in end_of_route:
            print(f"Game over! ({new_x}, {new_y})")
            exit()
        else:
            matrix[current_x][current_y], matrix[new_x][new_y] = matrix[new_x][new_y], matrix[current_x][current_y]


# relatively change of coordinates of the miner for given moving command:
commands = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0)
}
coal_coordinates = []
end_of_route = []
start_position = []

n = int(input())  # square matrix with n rows and columns
moving_commands = deque(command for command in input().split())  # collecting sequence of moving commands
matrix = [[element for element in input().split()] for _ in range(n)]  # generating matrix with input info

collecting_field_info(matrix)
[print(*row) for row in matrix]
print(" ")
moving_miner(moving_commands)
[print(*row) for row in matrix]