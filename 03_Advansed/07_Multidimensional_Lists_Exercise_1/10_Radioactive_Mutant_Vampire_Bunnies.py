def check_indexes(row, col):
    r = range(n)
    c = range(m)
    if row in r and col in c:
        return True
    else:
        return False


def check_if_player_won(row, col):
    global player_wins
    if not check_indexes(row, col):
        player_wins = True
        return True


def print_result(player_position, state_of_player):
    row = player_position[0]
    col = player_position[1]
    status = "dead"
    if state_of_player:
        status = "won"
    [print(*r, sep="") for r in lair]
    print(f"{status}: {row} {col}")
    exit()


def bunnies_spread(coordinates: set):
    new_bunnies = set()
    for coordinate in coordinates:
        for position in directions.values():
            bunny_x = coordinate[0] + position[0]
            bunny_y = coordinate[1] + position[1]
            if check_indexes(bunny_x, bunny_y):
                lair[bunny_x][bunny_y] = "B"
                new_bunnies.add((bunny_x, bunny_y))
    bunnies_coordinates.update(new_bunnies)


def check_if_player_dies(row, col):
    global player_wins
    if lair[row][col] == "B":
        player_wins = False
        return True


directions = {
    "U": (-1, 0),
    "D": (1, 0),
    "R": (0, 1),
    "L": (0, -1)
}
n, m = [int(x) for x in input().split()]  # rows  # columns
player_wins = False
lair = []
player_pos = []
bunnies_coordinates = set()
for row in range(n):
    lair.append(list(input()))
    if "P" in lair[row]:
        player_pos = [row, lair[row].index("P")]
        lair[row][lair[row].index("P")] = "."
    if "B" in lair[row]:
        bunny_pos = (row, lair[row].index("B"))
        bunnies_coordinates.add(bunny_pos)

commands = list(input())
for command in commands:
    row = player_pos[0] + directions[command][0]
    col = player_pos[1] + directions[command][1]

    check_if_player_won(row, col)
    bunnies_spread(bunnies_coordinates)

    if player_wins:
        print_result(player_pos, player_wins)
    else:
        player_pos = [row, col]

    if not player_wins and check_if_player_dies(row, col):
        print_result(player_pos, player_wins)
