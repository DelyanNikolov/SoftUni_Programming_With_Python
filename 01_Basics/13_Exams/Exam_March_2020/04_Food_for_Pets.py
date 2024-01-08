days_count = int(input())
total_food_amount = float(input())
cookies = 0
food_eaten = 0
dog_food = 0
cat_food = 0
daily_food = 0
for day in range(1, days_count + 1):

    dog_portion = int(input())
    cat_portion = int(input())
    dog_food += dog_portion
    cat_food += cat_portion
    food_eaten += (dog_portion + cat_portion)
    daily_food = dog_portion + cat_portion
    if day % 3 == 0:
        cookies += daily_food * 0.1

percentage_food_eaten = food_eaten / total_food_amount * 100
percentage_dog_food = dog_food / food_eaten * 100
percentage_cat_food = cat_food / food_eaten * 100
print(f"Total eaten biscuits: {round(cookies)}gr.")
print(f"{percentage_food_eaten :.2f}% of the food has been eaten.")
print(f"{percentage_dog_food :.2f}% eaten from the dog.")
print(f"{percentage_cat_food :.2f}% eaten from the cat.")
