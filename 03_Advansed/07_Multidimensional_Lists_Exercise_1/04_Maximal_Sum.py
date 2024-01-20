rows, cols = [int(el) for el in input().split()]
matrix = [[int(x) for x in input().split()] for _ in range(rows)]

maximum_sum = float("-Inf")
elements_of_max_sum = []

for row in range(rows - 2):
    for col in range(cols - 2):
        first_row = matrix[row][col: col + 3]
        second_row = matrix[row + 1][col: col + 3]
        third_row = matrix[row + 2][col: col + 3]

        sub_matrix_sum = sum(first_row) + sum(second_row) + sum(third_row)
        if sub_matrix_sum > maximum_sum:
            maximum_sum = sub_matrix_sum
            elements_of_max_sum = [first_row, second_row, third_row]

print(f"Sum = {maximum_sum}")
[print(*row) for row in elements_of_max_sum]
