from collections import deque

quantity_of_food = int(input())
orders = deque()
information = [int(item) for item in input().split()]
print(max(information))
for item in information:
    orders.append(item)

while True:
    if len(orders) > 0:
        serving = orders[0]
    else:
        break
    if quantity_of_food >= serving:
        orders.popleft()
        quantity_of_food -= serving
    else:
        quantity_of_food -= serving
        break
result = []
if quantity_of_food > 0:
    print("Orders complete")
else:
    for i in range(len(orders)):
        result.append(orders.popleft())
    print(f"Orders left: {' '.join(map(str, result))}")
