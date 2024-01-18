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
        flatten_square = []
        for i in range(square_side):
            flatten_square.extend(matrix[row_idx + i][col_idx:col_idx + square_side])
        sub_matrix_total += sum(flatten_square)
        if max_square_sum < sub_matrix_total:
            max_square_sum = sub_matrix_total
            max_square_numbers.append(flatten_square)
print(*max_square_numbers[-1][:square_side])
print(*max_square_numbers[-1][square_side:])
print(max_square_sum)
