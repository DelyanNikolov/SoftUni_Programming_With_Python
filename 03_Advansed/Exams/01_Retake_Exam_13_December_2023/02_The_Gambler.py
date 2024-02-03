def print_game_board():
    [print(*g, sep="") for g in game_board]


directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}
money_amount = 100
size = int(input())

player_pos = []

game_board = []
for r in range(size):
    game_board.append(list(input()))
    if "G" in game_board[r]:
        player_pos = [r, game_board[r].index("G")]
        game_board[r][game_board[r].index("G")] = "-"
command = input()
while command != "end":
    game_board[player_pos[0]][player_pos[1]] = "-"
    row = player_pos[0] + directions[command][0]
    col = player_pos[1] + directions[command][1]
    try:
        cell = game_board[row][col]
    except IndexError:
        print("Game over! You lost everything!")
        break
    game_board[row][col] = "G"

    if cell == "W":
        money_amount += 100
    elif cell == "P":
        money_amount -= 200
        if money_amount <= 0:
            print("Game over! You lost everything!")
            break
    elif cell == "J":
        money_amount += 100000
        print(f"You win the Jackpot!")
        print(f"End of the game. Total amount: {money_amount}$")
        print_game_board()
        break
    player_pos = [row, col]
    command = input()
else:
    print(f"End of the game. Total amount: {money_amount}$")
    print_game_board()
