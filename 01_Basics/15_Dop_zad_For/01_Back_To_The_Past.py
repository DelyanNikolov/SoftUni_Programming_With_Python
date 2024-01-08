
money = float(input())
year = int(input())

starting_age = 18
current_age = 17
for current_year in range(1800, year + 1):
    current_age += 1
    if current_year % 2 == 0:
        money -= 12000
    else:
        money -= 12000 + (50 * current_age)

if money >= 0:
    print(f"Yes! He will live a carefree life and will have {money:.2f} dollars left.")
else:
    print(f"He will need {abs(money):.2f} dollars to survive.")
