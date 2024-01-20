rows, cols = [int(el) for el in input().split()]
matrix = [input().split() for _ in range(rows)]

result = 0

for row in range(rows - 1):
    for col in range(cols - 1):
        element = matrix[row][col]
        if element == matrix[row][col + 1] and element == matrix[row + 1][col] and element == matrix[row + 1][col + 1]:
            result += 1
print(result)
