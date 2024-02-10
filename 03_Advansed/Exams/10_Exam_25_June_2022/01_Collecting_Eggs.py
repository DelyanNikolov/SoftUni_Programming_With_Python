from collections import deque

eggs_sizes = deque([int(e) for e in input().split(", ")])
paper_sizes = deque([int(p) for p in input().split(", ")])

boxes_filled = 0

while eggs_sizes and paper_sizes:

    egg = eggs_sizes.popleft()

    if egg == 13:
        pap_1 = paper_sizes.popleft()
        pap_2 = paper_sizes.pop()
        paper_sizes.append(pap_1)
        paper_sizes.appendleft(pap_2)
        continue

    elif egg <= 0:
        continue

    paper = paper_sizes.pop()
    value = egg + paper

    if value <= 50:
        boxes_filled += 1

if boxes_filled:
    print(f"Great! You filled {boxes_filled} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")
if eggs_sizes:
    print(f"Eggs left: {', '.join(map(str, eggs_sizes))}")
if paper_sizes:
    print(f"Pieces of paper left: {', '.join(map(str, paper_sizes))}")
