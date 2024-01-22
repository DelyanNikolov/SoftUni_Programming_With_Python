n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
bombs_coordinates = ((int(x) for x in c.split(",")) for c in input().split())

for row, col in bombs_coordinates:
    if matrix[row][col] <= 0:
        continue

    bomb_value = matrix[row][col]

    for x in range(-1, 2):
        for y in range(-1, 2):
            r, c = row + x, col + y
            if 0 <= r < n and 0 <= c < n:
                matrix[r][c] -= bomb_value if matrix[r][c] > 0 else 0

alive_cells = [num for row in range(n) for num in matrix[row] if num > 0]

print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")

[print(*row) for row in matrix]
