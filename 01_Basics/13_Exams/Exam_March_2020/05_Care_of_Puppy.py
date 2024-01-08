food_bought = int(input())
food_bought_grams = food_bought * 1000
total_food_eaten = 0
command = input()
enough_food = False
while command != "Adopted":
    daily_food = int(command)
    total_food_eaten += daily_food
    command = input()

if total_food_eaten <= food_bought_grams:
    enough_food = True
leftovers = abs(food_bought_grams - total_food_eaten)

if enough_food:
    print(f"Food is enough! Leftovers: {leftovers} grams.")
else:
    print(f"Food is not enough. You need {leftovers} grams more.")
