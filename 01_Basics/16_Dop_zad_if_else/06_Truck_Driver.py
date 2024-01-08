
season = input() #"Spring", "Summer", "Autumn" или "Winter"
kilometers_per_month = float(input())

price_per_km = 0
taxes = 0.1
if 10000 < kilometers_per_month <= 20000:
    price_per_km = 1.45

if season == "Spring" or season == "Autumn":
    if kilometers_per_month <= 5000:
        price_per_km = 0.75
    elif kilometers_per_month <= 10000:
        price_per_km = 0.95
elif season == "Summer":
    if kilometers_per_month <= 5000:
        price_per_km = 0.90
    elif kilometers_per_month <= 10000:
        price_per_km = 1.10
elif season == "Winter":
    if kilometers_per_month <= 5000:
        price_per_km = 1.05
    elif kilometers_per_month <= 10000:
        price_per_km = 1.25

salary = kilometers_per_month * price_per_km * 4 * (1 - taxes)

print(f"{salary:.2f}")
