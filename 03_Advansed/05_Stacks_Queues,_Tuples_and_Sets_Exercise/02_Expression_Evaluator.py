from collections import deque

expression = deque(input().split())
print(expression)

idx = 0

while idx < len(expression):
    element = expression[idx]
    if element == "-":
        for _ in range(idx - 1):
            expression.appendleft(int(expression.popleft()) - int(expression.popleft()))
    if element in "-+*/":
        del expression[1]
        idx = 1
    idx += 1