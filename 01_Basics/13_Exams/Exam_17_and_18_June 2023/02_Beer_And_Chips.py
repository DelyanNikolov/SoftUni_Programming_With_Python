
# •	На първия ред - името на футболният фен – текст
# •	На втория ред - предвиденият бюджет  – реално число в диапазона [1.0… 100 000.0]
# •	На третия ред - брой бутилки бира – цяло число в диапазона [1… 100 000]
# •	На четвърти ред - брой пакети чипс – цяло число в диапазона [1… 100 000]
from math import ceil
name_of_football_fan = input()
budget = float(input())
beers_count = int(input())
chips_count = int(input())

beer_price = 1.2
beer_cost = beers_count * beer_price
chips_price = 0.45 * beer_cost
chips_cost = ceil(chips_count * chips_price)

snack_cost = beer_cost + chips_cost
money_left = abs(budget - snack_cost)
if snack_cost <= budget:
    print(f"{name_of_football_fan} bought a snack and has {money_left :.2f} leva left.")
else:
    print(f"{name_of_football_fan} needs {money_left :.2f} more leva!")
