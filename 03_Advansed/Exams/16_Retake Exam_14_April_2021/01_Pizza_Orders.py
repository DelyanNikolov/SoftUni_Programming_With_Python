from collections import deque

pizza_orders = deque([int(p) for p in input().split(", ")])
employees_capacities = [int(e) for e in input().split(", ")]

pizzas_made = 0

while pizza_orders and employees_capacities:
    if pizza_orders[0] <= 0 or 10 < pizza_orders[0]:
        order = pizza_orders.popleft()
        continue
    else:
        order = pizza_orders.popleft()
    employee = employees_capacities.pop()

    if order <= employee:
        pizzas_made += order
    else:
        pizzas_made += employee
        order -= employee
        pizza_orders.appendleft(order)

if not pizza_orders:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {pizzas_made}")
    print(f"Employees: {', '.join(map(str, employees_capacities))}")
else:
    print(f"Not all orders are completed.")
    print(f"Orders left: {', '.join(map(str, pizza_orders))}")
