from collections import deque

worms = [int(x) for x in input().split()]
worms_count = len(worms)
holes = deque(int(y) for y in input().split())
worms_fit_count = 0
while worms and holes:
    worm = worms.pop()
    hole = holes.popleft()

    if worm == hole:
        worms_fit_count += 1
    else:
        worm -= 3
        if worm > 0:
            worms.append(worm)
        else:
            continue

if worms_fit_count:
    print(f"Matches: {worms_fit_count}")
else:
    print("There are no matches.")
if not worms and worms_fit_count >= worms_count:
    print("Every worm found a suitable hole!")
if not worms and worms_fit_count < worms_count:
    print("Worms left: none")
if worms:
    print(f"Worms left: {', '.join(str(w) for w in worms)}")
if holes:
    print(f"Holes left: {', '.join(str(w) for w in holes)}")
else:
    print("Holes left: none")
