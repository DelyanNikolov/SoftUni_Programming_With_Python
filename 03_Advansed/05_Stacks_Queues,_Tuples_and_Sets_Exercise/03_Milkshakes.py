from collections import deque

chocolates = [int(c) for c in input().split(", ")]
cups_of_milk = deque(int(x) for x in input().split(", "))

milkshakes = 0

while milkshakes < 5 and chocolates and cups_of_milk:
    chocolate = chocolates.pop()
    milk_cup = cups_of_milk.popleft()

    if chocolate <= 0 and milk_cup <= 0:
        milkshakes += 1
        continue
    elif chocolate <= 0:
        cups_of_milk.appendleft(milk_cup)
        continue
    elif milk_cup <= 0:
        chocolates.append(chocolate)
        continue

    if chocolate == milk_cup:
        milkshakes += 1
    else:
        cups_of_milk.append(milk_cup)
        chocolates.append(chocolate - 5)

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

print(f"Chocolate: {', '.join(str(x) for x in chocolates) or 'empty'}")
print(f"Milk: {', '.join(str(x) for x in cups_of_milk) or 'empty'}")

