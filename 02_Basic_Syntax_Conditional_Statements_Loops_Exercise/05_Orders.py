orders_count = int(input())
total_price = 0
for order in range(orders_count):
    capsule_price = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if not 0.01 <= capsule_price <= 100 or not 1 <= days <= 31 or not 1 <= capsules_per_day <= 2000:
        continue
    price = capsule_price * capsules_per_day * days
    total_price += price
    print(f"The price for the coffee is: ${price:.2f}")
print(f"Total: ${total_price:.2f}")
