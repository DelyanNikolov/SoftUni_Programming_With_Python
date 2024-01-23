
rows = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(rows)]

command = input().split()
while command[0] != "END":
    command_type, x1, y1, value = command[0], int(command[1]), int(command[2]), int(command[3])
    if 0 <= x1 < rows and 0 <= y1 < rows:
        if command_type == "Add":
            matrix[x1][y1] += value
        elif command_type == "Subtract":
            matrix[x1][y1] -= value
    else:
        print("Invalid coordinates")

    command = input().split()

[print(*row) for row in matrix]
