from collections import deque

cups = deque(int(cup) for cup in input().split())     # are que
bottles = [int(bot) for bot in input().split()]       # are stack
wasted_water = 0

while cups and bottles:
    current_cup = cups.popleft()
    current_bottle = bottles.pop()
    if current_cup >= current_bottle:
        current_cup -= current_bottle
        if current_cup > 0:
            cups.appendleft(current_cup)
    else:
        wasted_water += current_bottle - current_cup
if not cups:
    print(f"Bottles:", *bottles)
if not bottles:
    print(f"Cups:", *cups)
print(f"Wasted litters of water: {wasted_water}")
