items_list = input().split("|")
budget = float(input())
items_bought = []
for item_index in range(len(items_list)):
    data = items_list[item_index].split("->")
    item_type = data[0]
    item_price = float(data[1])
    if item_type == "Clothes" and item_price > 50:
        continue
    elif item_type == "Shoes" and item_price > 35:
        continue
    elif item_type == "Accessories" and item_price > 20.5:
        continue
    else:
        if item_price <= budget:
            items_bought.append(item_price)
            budget -= item_price
        else:
            continue

new_prices = [price * 1.4 for price in items_bought]
profit = sum(new_prices) - sum(items_bought)
new_budget = budget + sum(new_prices)

for i in range(len(new_prices)):
    print(f"{new_prices[i]:.2f}", end=" ")

print(f"\nProfit: {profit:.2f}")
if new_budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
