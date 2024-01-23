size = int(input())
matrix = [list(input()) for _ in range(size)]

position_numbers = [-2, -1, 1, 2]
positions = [(x, y) for x in position_numbers for y in position_numbers if abs(x) != abs(y)]

removed_knights = 0

while True:
    max_attacks = 0
    knight_with_most_attacks_pos = []

    for row in range(size):
        for col in range(size):
            if matrix[row][col] == "K":
                attack = 0
                for pos in positions:
                    pos_row = row + pos[0]
                    pos_col = col + pos[1]

                    if 0 <= pos_row < size and 0 <= pos_col < size:
                        if matrix[pos_row][pos_col] == "K":
                            attack += 1
                if attack > max_attacks:
                    knight_with_most_attacks_pos = [row, col]
                    max_attacks = attack

    if knight_with_most_attacks_pos:
        r, c = knight_with_most_attacks_pos
        matrix[r][c] = "0"
        removed_knights += 1
    else:
        break

print(removed_knights)
