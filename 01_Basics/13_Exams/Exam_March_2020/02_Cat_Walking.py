minutes_walk_per_day = int(input())
walks_count = int(input())
cat_calories_intake = int(input())

total_walking_time = walks_count * minutes_walk_per_day
calories_burned = total_walking_time * 5
target_calories = cat_calories_intake / 2

if calories_burned >= target_calories:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {calories_burned}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {calories_burned}.")
