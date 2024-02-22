from collections import deque

money_amounts = [int(x) for x in input().split()]
food_prices = deque([int(p) for p in input().split()])

food_bought = 0

while money_amounts and food_prices:
    money = money_amounts.pop()
    price = food_prices.popleft()

    if money == price:
        food_bought += 1
    elif money > price:
        change = money - price
        food_bought += 1
        if money_amounts:
            money_amounts[-1] += change

if food_bought >= 4:
    print(f"Gluttony of the day! Henry ate {food_bought} foods.")
elif 1 < food_bought < 4:
    print(f"Henry ate: {food_bought} foods.")
elif 0 < food_bought <= 1:
    print(f"Henry ate: {food_bought} food.")
else:
    print("Henry remained hungry. He will try next weekend again.")
