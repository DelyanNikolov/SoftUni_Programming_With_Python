dancers_count = int(input())
points_earned = float(input())
season = input()  # "summer" или "winter"
place = input()  # "Bulgaria" или "Abroad"
reward_money = 0
expenses = 0

if place == "Bulgaria":
    if season == "summer":
        expenses = 0.05
    elif season == "winter":
        expenses = 0.08
    reward_money = points_earned * dancers_count
    reward_money *= (1 - expenses)
elif place == "Abroad":
    if season == "summer":
        expenses = 0.1
    elif season == "winter":
        expenses = 0.15
    reward_money += points_earned * dancers_count * 1.5
    reward_money *= (1 - expenses)

sum_for_charity = 0.75 * reward_money
money_left = reward_money - sum_for_charity
money_per_dancer = money_left / dancers_count

print(f"Charity - {sum_for_charity :.2f}")
print(f"Money per dancer - {money_per_dancer :.2f}")
