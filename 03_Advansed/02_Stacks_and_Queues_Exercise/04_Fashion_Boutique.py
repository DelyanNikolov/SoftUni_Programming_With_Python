from collections import deque

clothes = deque([int(item) for item in input().split()])
rack_capacity = int(input())
racks_count = 1
new_rack_capacity = rack_capacity
while clothes:
    current_clothe = clothes.popleft()
    if new_rack_capacity < current_clothe:
        racks_count += 1
        new_rack_capacity = rack_capacity - current_clothe
    else:
        new_rack_capacity -= current_clothe
print(racks_count)
