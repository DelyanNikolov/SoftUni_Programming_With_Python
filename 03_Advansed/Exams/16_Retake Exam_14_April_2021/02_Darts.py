from collections import deque

size = 7

player_1, player_2 = input().split(", ")
players = deque([player_1, player_2])

scores = {player_1: 501, player_2: 501}

turns_count = 0
turn = 1
dartboard = []
for r in range(size):
    dartboard.append(input().split())

while True:
    turn += 1
    if turn % 2 == 0:
        turns_count += 1
    target = 0
    current_player = players[0]

    hit_pos = eval(input())
    row = hit_pos[0]
    col = hit_pos[1]

    if 0 <= row < size and 0 <= col < size:
        target = dartboard[row][col]
    else:
        players.rotate()
        continue

    if target.isdigit():
        scores[current_player] -= int(target)
    elif target == "D":
        points = 0
        for i in range(size):
            if dartboard[row][i].isdigit():
                points += int(dartboard[row][i])
        for j in range(size):
            if dartboard[j][col].isdigit():
                points += int(dartboard[j][col])
        points *= 2
        scores[current_player] -= points
        if scores[current_player] <= 0:
            print(f"{current_player} won the game with {turns_count} throws!")
            break
    elif target == "T":
        points = 0
        for i in range(size):
            if dartboard[row][i].isdigit():
                points += int(dartboard[row][i])
        for j in range(size):
            if dartboard[j][col].isdigit():
                points += int(dartboard[j][col])
        points *= 3
        scores[current_player] -= points
        if scores[current_player] <= 0:
            print(f"{current_player} won the game with {turns_count} throws!")
            break
    elif target == "B":
        print(f"{current_player} won the game with {turns_count} throws!")
        break

    players.rotate()
