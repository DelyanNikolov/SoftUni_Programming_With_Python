from collections import deque

working_bees = deque(int(b) for b in input().split())
nectar = [int(n) for n in input().split()]
symbols = deque(s for s in input().split())

functions = {
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b if b != 0 else 0,
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b
}

honey_made = 0

while working_bees and nectar:
    current_bee = working_bees.popleft()
    current_nectar = nectar.pop()

    if current_nectar < current_bee:
        working_bees.appendleft(current_bee)
    else:
        honey_made += abs(functions[symbols.popleft()](current_bee, current_nectar))

print(f"Total honey made: {honey_made}")
if working_bees:
    print(f"Bees left: {', '.join(str(x) for x in working_bees)}")
if nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")
