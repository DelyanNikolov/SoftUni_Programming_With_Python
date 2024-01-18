n = int(input())

matrix = []

for _ in range(n):
    matrix.append(list(input()))

searched_element = input()

for row_idx in range(n):
    for col_idx in range(len(matrix[row_idx])):
        if matrix[row_idx][col_idx] == searched_element:
            print(f"({row_idx}, {col_idx})")
            exit()
else:
    print(f"{searched_element} does not occur in the matrix")
