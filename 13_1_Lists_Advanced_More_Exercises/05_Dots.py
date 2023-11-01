rows_number = int(input())
field = []
for row in range(rows_number):
    row_info = input().split()
    field.append(row_info)

x_cor = 0
y_cor = 0
dot = "."
dash = "-"

connected = False
if field[x_cor][y_cor] == dot:
    if [x_cor][y_cor + 1] == dot:
        pass
    elif [x_cor][y_cor - 1] == dot:
        pass
    elif [x_cor + 1][y_cor] == dot:
        pass
    elif [x_cor - 1][y_cor] == dot:
        pass


def check_index():
    if 0 <= x_cor < len(field[0]) and x_cor + 1 < len(field):
        return True

