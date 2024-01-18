row_count = int(input())

matrix = []
for _ in range(row_count):
    matrix.append([int(el) for el in input().split()])

diagonal_sum = 0

for row_idx in range(row_count):
    diagonal_sum += matrix[row_idx][row_idx]

print(diagonal_sum)
