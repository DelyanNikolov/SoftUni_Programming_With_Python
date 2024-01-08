budget = int(input())
season = input()  # "Spring", "Summer", "Autumn" или "Winter";
fishermen_count = int(input())

price_for_boat_rent = 0
discount_for_fishermen_count = 0
discount_for_even_number_fishermen = 0.05

if season == "Spring":
    price_for_boat_rent = 3000
    if 0 < fishermen_count <= 6:
        discount_for_fishermen_count = 0.1
    elif 7 <= fishermen_count <= 11:
        discount_for_fishermen_count = 0.15
    elif fishermen_count >= 12:
        discount_for_fishermen_count = 0.25
elif season == "Summer" or season == "Autumn":
    price_for_boat_rent = 4200
    if 0 < fishermen_count <= 6:
        discount_for_fishermen_count = 0.1
    elif 7 <= fishermen_count <= 11:
        discount_for_fishermen_count = 0.15
    elif fishermen_count >= 12:
        discount_for_fishermen_count = 0.25
elif season == "Winter":
    price_for_boat_rent = 2600
    if 0 < fishermen_count <= 6:
        discount_for_fishermen_count = 0.1
    elif 7 <= fishermen_count <= 11:
        discount_for_fishermen_count = 0.15
    elif fishermen_count >= 12:
        discount_for_fishermen_count = 0.25

cost_of_boat = (price_for_boat_rent * (1 - discount_for_fishermen_count))

if fishermen_count % 2 == 0 and season != "Autumn":
    discount_for_even_number_fishermen = 0.05
else:
    discount_for_even_number_fishermen = 0

cost_of_boat = cost_of_boat * (1 - discount_for_even_number_fishermen)

if budget >= cost_of_boat:
    print(f"Yes! You have {(budget - cost_of_boat):.2f} leva left.")
else:
    print(f"Not enough money! You need {(cost_of_boat - budget):.2f} leva.")
