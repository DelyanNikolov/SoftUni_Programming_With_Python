from collections import deque

kids_names = deque(input().split())
toss = int(input()) - 1
while len(kids_names) > 1:
    kids_names.rotate(-toss)
    kid = kids_names.popleft()
    print(f"Removed {kid}")

print(f"Last is {kids_names[0]}")
