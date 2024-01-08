budget = float(input())
season = input()

location = ""
place = ""
cost_of_vacation = 0

if budget <= 1000:
    place = "Camp"
    if season == "Summer":
        cost_of_vacation = budget * 0.65
        location = "Alaska"
    elif season == "Winter":
        cost_of_vacation = budget * 0.45
        location = "Morocco"

elif 1000 < budget <= 3000:
    place = "Hut"
    if season == "Summer":
        cost_of_vacation = budget * 0.80
        location = "Alaska"
    elif season == "Winter":
        cost_of_vacation = budget * 0.60
        location = "Morocco"
elif budget > 3000:
    place = "Hotel"
    if season == "Summer":
        cost_of_vacation = budget * 0.90
        location = "Alaska"
    elif season == "Winter":
        cost_of_vacation = budget * 0.90
        location = "Morocco"


print(f"{location} - {place} - {cost_of_vacation:.2f}")
