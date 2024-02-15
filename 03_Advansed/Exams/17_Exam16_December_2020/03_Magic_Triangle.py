def get_magic_triangle(row_count):
    triangle = [[1], [1, 1]]
    for row in range(2, row_count):
        new_row = []
        for el in range(row + 1):
            first_el = 0
            second_el = 0
            if 0 <= (row - 1) <= len(triangle) and 0 <= (el - 1) <= len(triangle):
                first_el = triangle[row - 1][el - 1]

            if 0 <= (row - 1) <= len(triangle) and 0 <= (el + 1) <= len(triangle):
                second_el = triangle[row - 1][el]
            new_element = first_el + second_el
            new_row.append(new_element)
        triangle.append(new_row)
    return triangle


get_magic_triangle(5)
