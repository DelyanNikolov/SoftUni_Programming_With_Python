from collections import deque
from math import floor

expression = deque(input().split())

idx = 0

while idx < len(expression):
    element = expression[idx]
    if element == "*":
        for _ in range(idx - 1):
            expression.appendleft(int(expression.popleft()) * int(expression.popleft()))
    elif element == "/":
        for _ in range(idx - 1):
            expression.appendleft(int(expression.popleft()) / int(expression.popleft()))
    elif element == "-":
        for _ in range(idx - 1):
            expression.appendleft(int(expression.popleft()) - int(expression.popleft()))
    elif element == "+":
        for _ in range(idx - 1):
            expression.appendleft(int(expression.popleft()) + int(expression.popleft()))

    if element in "/*+-":
        del expression[1]
        idx = 1

    idx += 1

print(floor(int(expression[0])))
#
# from functools import reduce
# from math import floor
#
# # expression = input().split()  # [6, 5, 4, 5, +]
# #
# # idx = 0
#
# functions = {
#     "*": lambda i: reduce(lambda a, b: a * b, map(int, expression[:i])),
#     "/": lambda i: reduce(lambda a, b: a / b, map(int, expression[:i])),
#     "-": lambda i: reduce(lambda a, b: a - b, map(int, expression[:i])),
#     "+": lambda i: reduce(lambda a, b: a + b, map(int, expression[:i])),
# }
#
# # [1, 2, +, 4, 5, -]
# # [3, 4, 5, -]
#
# while idx < len(expression):
#     element = expression[idx]
#
#     if element in "/*+-":
#         expression[0] = functions[element](idx)
#         [expression.pop(1) for _ in range(idx)]  # pop everything including the symbol
#         idx = 1
#
#     idx += 1
#
# print(floor(int(expression[0])))
