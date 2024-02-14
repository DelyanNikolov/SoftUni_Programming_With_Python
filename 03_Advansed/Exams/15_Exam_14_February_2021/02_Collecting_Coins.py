from math import floor

directions = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
    }
size = int(input())

player_pos = None
player_path = []
score = 0
player_lost = False

field = []
for row in range(size):
    field.append(input().split())
    if "P" in field[row]:
        player_pos = row, field[row].index("P")

player_path.append(list(player_pos))

while True:
    command = input()

    if command not in directions.keys():
        continue
    current_row, current_col = player_pos[0], player_pos[1]

    # if not (0 <= desired_row < size and 0 <= desired_col < size):
    desired_row = (current_row + directions.get(command)[0]) % size
    desired_col = (current_col + directions.get(command)[1]) % size

    element = field[desired_row][desired_col]

    if element.isdigit():
        score += int(element)
        field[desired_row][desired_col] = "0"
    elif element == "X":
        score = floor((score / 2))
        player_lost = True
        player_pos = desired_row, desired_col
        player_path.append(list(player_pos))
        break
    player_pos = desired_row, desired_col
    player_path.append(list(player_pos))
    if score >= 100:
        break
if player_lost or score < 100:
    print(f"Game over! You've collected {score} coins.")
elif not player_lost and score >= 100:
    print(f"You won! You've collected {score} coins.")
print("Your path:")
for coordinates in player_path:
    print(coordinates)
