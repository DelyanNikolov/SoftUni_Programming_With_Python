from collections import deque

males = [int(m) for m in input().split()]
females = deque([int(f) for f in input().split()])

matches_count = 0

while males and females:
    if males[-1] <= 0:
        males.pop()
        continue
    if females[0] <= 0:
        females.popleft()
        continue

    if males[-1] % 25 == 0:
        males.pop()
        males.pop()
        continue

    if females[0] % 25 == 0:
        females.popleft()
        females.popleft()
        continue

    if males[-1] == females[0]:
        male = males.pop()
        female = females.popleft()
        matches_count += 1
    else:
        females.popleft()
        males[-1] -= 2

print(f"Matches: {matches_count}")
if males:
    print(f"Males left: {', '.join(map(str, males[::-1]))}")
else:
    print(f"Males left: none")
if females:
    print(f"Females left: {', '.join(map(str, females))}")
else:
    print(f"Females left: none")
