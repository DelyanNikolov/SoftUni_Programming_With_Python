# •	Бензин – 2.22 лева за един литър,
# •	Дизел – 2.33 лева за един литър
# •	Газ – 0.93 лева за литър
GASOLINE = 2.22
DIESEL = 2.33
LPG = 0.93
# Ако водача има карта за отстъпки,  той се възползва от следните намаления за литър гориво:
# 18 ст. за литър бензин, 12 ст. за литър дизел и 8 ст. за литър газ.
# Ако шофьора е заредил между 20 и 25 литра включително, той получава 8 процента отстъпка от крайната цена,
# при повече от 25 литра гориво, той получава 10 процента отстъпка от крайната цена.

GASOLINE_DISCOUNT = 0.18
DIESEL_DISCOUNT = 0.12
LPG_DISCOUNT = 0.08
LITERS_DISCOUNT_20_25 = 0.08
LITERS_DISCOUNT_OVER_25 = 0.1

# Входът се чете от конзолата и се състои от 3 реда:
# •	Типа на горивото – текст с възможности: "Gas", "Gasoline" или "Diesel"
# •	Количество гориво – реално число в интервала [1.00 … 50.00]
# •	Притежание на клубна карта – текст с възможности: "Yes" или "No"
# На конзолата трябва да се отпечата един ред.
# •	"{крайната цена на горивото} lv."
# Цената на горивото да бъде форматираната до втората цифра след десетичния знак.

fuel_type = input()
liters_fuel = float(input())
discount_card = input()

fuel_price = 0
fuel_price_after_discounts = 0

if fuel_type == "Gas":
    if discount_card == "Yes":
        fuel_price = liters_fuel * (LPG - LPG_DISCOUNT)
    else:
        fuel_price = liters_fuel * LPG

elif fuel_type == "Gasoline":
    if discount_card == "Yes":
        fuel_price = liters_fuel * (GASOLINE - GASOLINE_DISCOUNT)
    else:
        fuel_price = liters_fuel * GASOLINE

elif fuel_type == "Diesel":
    if discount_card == "Yes":
        fuel_price = liters_fuel * (DIESEL - DIESEL_DISCOUNT)
    else:
        fuel_price = liters_fuel * DIESEL

if liters_fuel > 25:
    fuel_price_after_discounts = fuel_price * (1 - LITERS_DISCOUNT_OVER_25)
elif liters_fuel < 20:
    fuel_price_after_discounts = fuel_price
else:
    fuel_price_after_discounts = fuel_price * (1 - LITERS_DISCOUNT_20_25)

print(f"{fuel_price_after_discounts:.2f} lv.")
