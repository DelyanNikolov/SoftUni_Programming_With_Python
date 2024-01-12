from collections import deque

quantity_of_food = int(input())
orders = deque([int(item) for item in input().split()])
print(max(orders))
while quantity_of_food > 0 and orders:
    food_needed = orders.popleft()
    if quantity_of_food >= food_needed:
        quantity_of_food -= food_needed
    else:
        orders.appendleft(food_needed)
        print("Orders left:", *orders)
        break
else:
    print("Orders complete")
