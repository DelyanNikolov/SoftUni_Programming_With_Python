
season = input()    #“Winter”, “Spring” или “Summer”;
group_type = input()    #“boys”, “girls” или “mixed”;
students_count = int(input())
nights = int(input())

price_per_night = 0
discount = 0
sport_type = ""

if season == "Winter":
    if group_type == "boys" or group_type == "girls":
        price_per_night = 9.60
        if group_type == "boys":
            sport_type = "Judo"
        elif group_type == "girls":
            sport_type = "Gymnastics"
    elif group_type == "mixed":
        price_per_night = 10.00
        sport_type = "Ski"
elif season == "Spring":
    if group_type == "boys" or group_type == "girls":
        price_per_night = 7.20
        if group_type == "boys":
            sport_type = "Tennis"
        elif group_type == "girls":
            sport_type = "Athletics"
    elif group_type == "mixed":
        price_per_night = 9.50
        sport_type = "Cycling"
elif season == "Summer":
    if group_type == "boys" or group_type == "girls":
        price_per_night = 15
        if group_type == "boys":
            sport_type = "Football"
        elif group_type == "girls":
            sport_type = "Volleyball"
    elif group_type == "mixed":
        price_per_night = 20
        sport_type = "Swimming"

if students_count >= 50:
    discount = 0.5
elif students_count >= 20:
    discount = 0.15
elif students_count >= 10:
    discount = 0.05

cost_of_vacation = price_per_night * students_count * nights * (1 - discount)
print(f"{sport_type} {cost_of_vacation:.2f} lv.")
