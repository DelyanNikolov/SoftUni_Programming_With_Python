size = 6
points = 0

board = []
for r in range(size):
    board.append(input().split())

for ball in range(3):
    ball_pos = [int(x) for x in input().strip("(").strip(")").split(", ")]

    row = ball_pos[0]
    col = ball_pos[1]

    if 0 <= row < size and 0 <= col < size:
        target = board[row][col]
        if target == "B":
            board[row][col] = 0
            for row_idx in range(size):
                element = board[row_idx][col]
                points += int(element)
    else:
        continue

prize = ""
if points < 100:
    prize = ""
elif 100 <= points < 200:
    prize = "Football"
elif 200 <= points < 300:
    prize = "Teddy Bear"
elif 300 <= points:
    prize = "Lego Construction Set"

if prize:
    print(f"Good job! You scored {points} points, and you've won {prize}.")
else:
    print(f"Sorry! You need {100 - points} points more to win a prize.")
