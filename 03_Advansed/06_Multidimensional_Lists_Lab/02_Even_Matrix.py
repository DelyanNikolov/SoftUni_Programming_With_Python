rows_count = int(input())

matrix = []

for i in range(rows_count):
    row_data = [int(el) for el in input().split(",") if int(el) % 2 == 0]
    matrix.append(row_data)

print(matrix)
