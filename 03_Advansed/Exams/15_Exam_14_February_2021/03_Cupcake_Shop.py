from collections import deque


def stock_availability(items, command, *args):
    inventory = deque(items)
    if command == "delivery":
        for product in args:
            inventory.append(product)

    elif command == "sell":
        if not args:
            inventory.popleft()

        elif str(args[0]).isdigit():
            for _ in range(args[0]):
                inventory.popleft()
        else:
            for cupcake in args:
                if cupcake in inventory:
                    inventory = [item for item in inventory if item != cupcake]

    return list(inventory)


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
