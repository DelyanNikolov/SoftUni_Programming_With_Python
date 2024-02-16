from collections import deque

clock_cycle = 0

jobs = enumerate([int(x) for x in input().split(", ")])
searched_idx = int(input())
data = list(jobs)
data.sort(key=lambda x: (x[1], x[0]))
sorted_data = deque(data)
while True:
    item = sorted_data.popleft()
    idx = item[0]
    clock = item[1]
    if idx == searched_idx:
        clock_cycle += clock
        break
    else:
        clock_cycle += clock
print(clock_cycle)