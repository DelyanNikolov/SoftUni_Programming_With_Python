import math

MAGNOLIAS = 3.25
HYACINTH = 4
ROSE = 3.5
CACTUS = 8
TAXES = 0.05
magnolias_count = int(input())
hyacinth_count = int(input())
rose_count = int(input())
cactus_count = int(input())
price_of_present = float(input())

profit = (magnolias_count * MAGNOLIAS + hyacinth_count * HYACINTH
          + rose_count * ROSE
          + cactus_count * CACTUS) * (1 - TAXES)

money_left = abs(profit - price_of_present)

if profit >= price_of_present:
    print(f"She is left with {math.floor(money_left)} leva.")
else:
    print(f"She will have to borrow {math.ceil(money_left)} leva.")
