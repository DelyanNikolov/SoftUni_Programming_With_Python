from collections import deque

customers = deque()
while True:
    customer_name = input()
    if customer_name == "End":
        break
    elif customer_name == "Paid":
        while customers:
            print(customers.popleft())
    else:
        customers.append(customer_name)
print(f"{len(customers)} people remaining.")
