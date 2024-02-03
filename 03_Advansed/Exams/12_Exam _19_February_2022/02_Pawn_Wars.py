SIZE = 8

chess_board = []
white_pawn_pos = []
black_pawn_pos = []

for row in range(SIZE):
    chess_board.append([x for x in input().split()])
    if "w" in chess_board[row]:
        white_pawn_pos = [row, chess_board[row].index("w")]
    if "b" in chess_board[row]:
        black_pawn_pos = [row, chess_board[row].index("b")]

positions = [white_pawn_pos, black_pawn_pos]

if abs(positions[0][1] - positions[1][1]) != 1:
    if SIZE - positions[0][0] - 1 <= positions[1][0]:
        print(f"Game over! Black pawn is promoted to a queen at {chr(97 + positions[1][1])}1.")
    else:
        print(f"Game over! White pawn is promoted to a queen at {chr(97 + positions[0][1])}8.")
else:
    place = (positions[0][0] + positions[1][0]) // 2
    if positions[0][0] % 2 == positions[1][0] % 2:
        print(f"Game over! Black win, capture on {chr(97 + positions[0][1])}{SIZE - place}.")
    else:
        print(f"Game over! White win, capture on {chr(97 + positions[1][1])}{SIZE - place}.")
