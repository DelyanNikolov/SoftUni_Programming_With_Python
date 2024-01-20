from collections import deque

rows, cols = [int(x) for x in input().split()]
snake_string = list(input())

word = deque(snake_string)
for row in range(rows):
    while len(word) < cols:
        word.extend(snake_string)

    if row % 2 == 0:
        print(*[word.popleft() for _ in range(cols)], sep="")
    else:
        print(*[word.popleft() for _ in range(cols)][::-1], sep="")
