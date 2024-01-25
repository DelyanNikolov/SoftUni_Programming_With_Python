from collections import deque

directions = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0)
}
total_coal_in_matrix = 0
coal_collected = 0
matrix = []
miner_pos = []
n = int(input())  # square matrix with n rows and columns
moving_commands = deque(command for command in input().split())  # collecting sequence of moving commands
for row in range(n):  # generating matrix with input info
    matrix.append(input().split())
    if "s" in matrix[row]:
        miner_pos = [row, matrix[row].index("s")]
    total_coal_in_matrix += matrix[row].count("c")

while moving_commands:
    command = moving_commands.popleft()
    r = miner_pos[0] + directions[command][0]
    c = miner_pos[1] + directions[command][1]
    if 0 <= r < n and 0 <= c < n:
        miner_pos = [r, c]
        field = matrix[r][c]
        if field == "c":
            coal_collected += 1
            matrix[r][c] = "*"
            if coal_collected == total_coal_in_matrix:
                print(f"You collected all coal! ({miner_pos[0]}, {miner_pos[1]})")
                break
        elif field == "e":
            print(f"Game over! ({miner_pos[0]}, {miner_pos[1]})")
            break
else:
    print(f"{total_coal_in_matrix - coal_collected} pieces of coal left. ({miner_pos[0]}, {miner_pos[1]})")
