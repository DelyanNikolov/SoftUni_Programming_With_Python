def check_indices(ind):
    """ checks if the coordinates are valid indices in the matrix"""
    return {ind[0], ind[2]}.issubset(valid_rows) and {ind[1], ind[3]}.issubset(valid_columns)


def swap_elements(command_type, indices):
    """checks is the command row valid and prints the matrix changes or error msg"""
    if command_type == "swap" and len(indices) == 4 and check_indices(indices):
        row1, col1, row2, col2 = indices
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        [print(*row) for row in matrix]
    else:
        print("Invalid input!")


rows, cols = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(rows)]

valid_rows = range(rows)
valid_columns = range(cols)

while True:
    command, *coordinates = [int(x) if x.isdigit() else x for x in input().split()]

    if command == "END":
        break
    swap_elements(command, coordinates)
