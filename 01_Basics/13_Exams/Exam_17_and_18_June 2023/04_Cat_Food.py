# •	На първи ред - броят на котките - цяло число в интервала [1..100]
# •	На всеки следващ ред за всяка котка - Х грама храна - реално число в интервала [100.00..400.00]
group_1 = 0
group_2 = 0
group_3 = 0
food_per_day_grams = 0
cats_count = int(input())
for _ in range(cats_count):
    current_food_grams = float(input())
    food_per_day_grams += current_food_grams
    if 100 <= current_food_grams < 200:
        group_1 += 1
    elif 200 <= current_food_grams < 300:
        group_2 += 1
    elif 300 <= current_food_grams < 400:
        group_3 += 1

price_of_food = food_per_day_grams / 1000 * 12.45
print(f"Group 1: {group_1} cats.")
print(f"Group 2: {group_2} cats.")
print(f"Group 3: {group_3} cats.")
print(f"Price for food per day: {price_of_food :.2f} lv.")
