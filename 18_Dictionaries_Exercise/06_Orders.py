orders = {}
command = input().split()
while not command[0] == "buy":
    name, price, quantity = command[0], float(command[1]), int(command[2])
    if name not in orders.keys():
        orders[name] = [price, quantity]
    else:
        orders[name][0] = price
        orders[name][1] += quantity
    command = input().split()

for product, info in orders.items():
    total_price = orders[product][0] * orders[product][1]
    print(f"{product} -> {total_price:.2f}")
