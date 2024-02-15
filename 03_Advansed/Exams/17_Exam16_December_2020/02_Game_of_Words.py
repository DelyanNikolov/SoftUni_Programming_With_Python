directions = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
    }

text = input()
size = int(input())

player_pos = None

field = []
for row in range(size):
    field.append(list(input()))
    if "P" in field[row]:
        player_pos = row, field[row].index("P")

m = int(input())

for _ in range(m):
    direction = input()
    current_row = player_pos[0]
    current_col = player_pos[1]
    desired_row = player_pos[0] + directions[direction][0]
    desired_col = player_pos[1] + directions[direction][1]
    if 0 <= desired_row < size and 0 <= desired_col < size:
        element = field[desired_row][desired_col]
        field[current_row][current_col] = "-"
        field[desired_row][desired_col] = "P"
        player_pos = desired_row, desired_col
        if element.isalpha():
            text += element
    else:
        if text:
            text = text[:-1]

print(text)
[print(*line, sep="") for line in field]
