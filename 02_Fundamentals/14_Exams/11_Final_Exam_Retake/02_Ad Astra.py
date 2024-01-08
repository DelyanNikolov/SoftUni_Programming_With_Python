import re

some_text = input()
regex = r"([#|])([A-Za-z\s]+)(\1)(\d{2}\/\d{2}\/\d{2})(\1)(\d+)(\1)"
food_information = re.findall(regex, some_text)
info = []
food_name = ""
best_before = ""
nutrition = 0

total_calories = sum([int(item[5]) for item in food_information])
days = total_calories // 2000
print(f"You have food to last you for: {days} days!")
for food in food_information:
    food_name, best_before, nutrition = food[1], food[3], int(food[5])
    print(f"Item: {food_name}, Best before: {best_before}, Nutrition: {nutrition}")
