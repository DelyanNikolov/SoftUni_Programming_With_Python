from collections import deque

bows_of_ramen = [int(x) for x in input().split(", ")]
customers = deque([int(c) for c in input().split(", ")])

while bows_of_ramen and customers:
    bow = bows_of_ramen.pop()
    customer = customers.popleft()

    if bow == customer:
        continue

    elif bow > customer:
        bow -= customer
        bows_of_ramen.append(bow)

    elif bow < customer:
        customer -= bow
        customers.appendleft(customer)

if not customers:
    print("Great job! You served all the customers.")
    if bows_of_ramen:
        print(f"Bowls of ramen left: {', '.join(map(str, bows_of_ramen))}")
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(map(str, customers))}")
