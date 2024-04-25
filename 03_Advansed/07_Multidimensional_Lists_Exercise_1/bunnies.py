def move_player(command):
    row = player_pos[0] + directions[command][0]
    col = player_pos[1] + directions[command][1]
    return [row, col]


def bunnies_spread(coordinates: set):
    new_bunnies = set()
    for coordinate in coordinates:
        for position in directions.values():
            bunny_x = coordinate[0] + position[0]
            bunny_y = coordinate[1] + position[1]
            if bunny_x in range(n) and bunny_y in range(m):
                lair[bunny_x][bunny_y] = "B"
                new_bunnies.add((bunny_x, bunny_y))
    return new_bunnies


def change_player_status(position, bunnies_pos, n, m):
    global player_wins
    global player_alive
    row = position[0]
    col = position[1]

    for b_pos in bunnies_pos:
        if (row, col) == b_pos:
            player_alive = False

    if row not in range(n) or col not in range(m):
        player_wins = True


def print_result(player_position, state_of_player):
    row = player_position[0]
    col = player_position[1]
    status = "dead"
    if state_of_player:
        status = "won"
    [print(*r, sep="") for r in lair]
    print(f"{status}: {row} {col}")


directions = {
    "U": (-1, 0),
    "D": (1, 0),
    "R": (0, 1),
    "L": (0, -1)
}

n, m = [int(x) for x in input().split()]  # rows  # columns
player_wins = False
player_alive = True
lair = []
player_pos = []
bunnies_coordinates = set()
for r in range(n):
    lair.append(list(input()))
    if "P" in lair[r]:
        player_pos = [r, lair[r].index("P")]
        lair[r][lair[r].index("P")] = "."

    if "B" in lair[r]:
        bunny_pos = (r, lair[r].index("B"))
        bunnies_coordinates.add(bunny_pos)

commands = list(input())
for command in commands:
    current_pos = move_player(command)
    bunnies_coordinates.update(bunnies_spread(bunnies_coordinates))

    # displaying bunnies in lair
    # for bunny_p in bunnies_coordinates:
    #     x, y = bunny_p
    #     lair[x][y] = "B"

    change_player_status(current_pos, bunnies_coordinates, n, m)

    if not player_alive and not player_wins:
        print_result(current_pos, player_alive)
        break

    if player_wins and player_alive:
        print_result(player_pos, player_alive)
        break

    # player actually moves
    player_pos = current_pos
