
number_of_rows = int(input())
field = []
for row in range(number_of_rows):
    row_info = [int(r) for r in input().split()]
    field.append(row_info)

ships_destroyed = 0
attacks_order = input().split()
for attack in attacks_order:
    coordinates = attack.split("-")
    x_cor = int(coordinates[0])
    y_cor = int(coordinates[1])
    if field[x_cor][y_cor] > 0:
        field[x_cor][y_cor] -= 1
        if field[x_cor][y_cor] <= 0:
            ships_destroyed += 1
print(ships_destroyed)
