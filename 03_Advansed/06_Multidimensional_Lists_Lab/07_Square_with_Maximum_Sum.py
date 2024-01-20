rows, columns = [int(el) for el in input().split(",")]
square_side = 2

matrix = []
max_square_sum = float("-inf")
max_square_numbers = []
for _ in range(rows):
    matrix.append([int(x) for x in input().split(", ")])

for row_idx in range(rows - square_side + 1):
    for col_idx in range(len(matrix[row_idx]) - square_side + 1):
        sub_matrix_total = 0
        sub_matrix_elements = []
        for i in range(square_side):
            row = matrix[row_idx + i][col_idx:col_idx + square_side]
            sub_matrix_elements.append(row)
            sub_matrix_total += sum(row)
        if max_square_sum < sub_matrix_total:
            max_square_sum = sub_matrix_total
            max_square_numbers.clear()
            max_square_numbers.extend(sub_matrix_elements)


for element in max_square_numbers:
    print(*element)
print(max_square_sum)
