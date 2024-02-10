from collections import deque

players = deque(input().split(", "))
size = 6

maze = []
for r in range(size):
    maze.append(input().split())

resting_players = []

while True:
    next_pos = eval(input())
    element = maze[next_pos[0]][next_pos[1]]
    player = players[0]
    if player in resting_players:
        resting_players.remove(players[0])
        players.rotate()
        continue
    if element == "E":
        print(f"{player} found the Exit and wins the game!")
        break
    elif element == "T":
        print(f"{players[0]} is out of the game! The winner is {players[1]}.")
        break
    elif element == "W":
        print(f"{player} hits a wall and needs to rest.")
        resting_players.append(players[0])

    players.rotate()
