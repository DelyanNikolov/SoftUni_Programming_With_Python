budget = float(input())
season = input()

car_class = ""
car_type = ""
cost_of_car = 0

if budget <= 100:
    car_class = "Economy class"
    if season == "Summer":
        cost_of_car = budget * 0.35
        car_type = "Cabrio"
    elif season == "Winter":
        cost_of_car = budget * 0.65
        car_type = "Jeep"
elif 100 < budget <= 500:
    car_class = "Compact class"
    if season == "Summer":
        cost_of_car = budget * 0.45
        car_type = "Cabrio"
    elif season == "Winter":
        cost_of_car = budget * 0.80
        car_type = "Jeep"
elif budget > 500:
    car_class = "Luxury class"
    if season == "Summer":
        cost_of_car = budget * 0.9
        car_type = "Jeep"
    elif season == "Winter":
        cost_of_car = budget * 0.9
        car_type = "Jeep"

print(car_class)
print(f"{car_type} - {cost_of_car:.2f}")
