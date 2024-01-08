t_shirt_price = float(input())
bonus_sum = float(input())

shorts_price = t_shirt_price * 0.75
socks_price = shorts_price * 0.2
shoes_price = (t_shirt_price + shorts_price) * 2
discount = 0.15

total_price = (t_shirt_price + shorts_price + socks_price + shoes_price) * (1 - discount)

if total_price >= bonus_sum:
    print("Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {total_price :.2f} lv.")
else:
    diff = bonus_sum - total_price
    print("No, he will not earn the world-cup replica ball.")
    print(f"He needs {diff :.2f} lv. more.")
