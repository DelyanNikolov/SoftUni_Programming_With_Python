size = int(input())
matrix = []
teabags_collected = 0
alice_pos = []
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size):
    matrix.append(input().split())
    if "A" in matrix[row]:
        alice_pos = [row, matrix[row].index("A")]
        matrix[row][alice_pos[1]] = "*"

while teabags_collected < 10:
    command = input()
    row = alice_pos[0] + directions[command][0]
    col = alice_pos[1] + directions[command][1]
    if not (0 <= row < size and 0 <= col < size):
        break

    alice_pos = [row, col]
    element = matrix[row][col]
    matrix[row][col] = "*"
    if element == "R":
        break
    if element.isdigit():
        teabags_collected += int(element)

if teabags_collected >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

[print(*row)for row in matrix]
