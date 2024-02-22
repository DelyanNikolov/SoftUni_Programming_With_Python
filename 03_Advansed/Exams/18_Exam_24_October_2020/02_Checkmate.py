directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

chess_board = []
queens_pos = []
queens_can_capture = []
for row in range(8):
    chess_board.append(input().split())
    if "Q" in chess_board[row]:
        queens_pos.append((row, chess_board[row].index("Q")))

for queen in queens_pos:
    for direction in directions:
        q_row = queen[0]
        q_col = queen[1]
        queen_move = q_row, q_col
        queen_capture = False
        while True:
            if queen_capture:
                break
            next_row = queen_move[0] + direction[0]
            next_col = queen_move[1] + direction[1]
            if 0 <= next_row < 8 and 0 <= next_col < 8:
                element = chess_board[next_row][next_col]
                if element == "K":
                    queens_can_capture.append([queen[0], queen[1]])
                    queen_capture = True
                    break
                elif element == "Q":
                    break
                else:
                    queen_move = next_row, next_col
            else:
                break
if queens_can_capture:
    print(*queens_can_capture, sep="\n")
else:
    print("The king is safe!")
