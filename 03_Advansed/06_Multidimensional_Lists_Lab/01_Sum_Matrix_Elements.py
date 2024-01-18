row_count, column_count = [int(el) for el in input().split(", ")]
total_sum = 0

matrix = []
for i in range(row_count):

    row_data = [int(x) for x in input().split(", ")]
    total_sum += sum(row_data)

    matrix.append(row_data)

print(total_sum)
print(matrix)
