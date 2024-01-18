row_count, col_count = [int(x) for x in input().split(",")]

matrix = []
for row in range(row_count):
    row_data = [int(el) for el in input().split()]
    matrix.append(row_data)

for col_idx in range(col_count):
    col_sum = 0
    for row_idx in range(row_count):
        col_sum += matrix[row_idx][col_idx]
    print(col_sum)
