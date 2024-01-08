budget = float(input())
season = input()

type_of_vacation = ""
destination = ""
cost = 0

if season == "summer":
    type_of_vacation = "Camp"
elif season == "winter":
    type_of_vacation = "Hotel"

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        cost = budget * 0.3
    elif season == "winter":
        cost = budget * 0.7

if 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        cost = budget * 0.4
    elif season == "winter":
        cost = budget * 0.8

if budget > 1000:
    destination = "Europe"
    type_of_vacation = "Hotel"
    if season == "summer" or season == "winter":
        cost = budget * 0.9

print(f"Somewhere in {destination}")
print(f"{type_of_vacation} - {cost:.2f}")
