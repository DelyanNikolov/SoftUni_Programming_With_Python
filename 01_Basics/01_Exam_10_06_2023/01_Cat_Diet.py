fat_percentage = int(input())
protein_percentage = int(input())
carbs_percentage = int(input())
total_calories = float(input())
water_percentage = int(input())

fat_grams = fat_percentage / 100 * total_calories / 9
protein_grams = protein_percentage / 100 * total_calories / 4
carbs_grams = carbs_percentage / 100 * total_calories / 4

weight_of_food = fat_grams + protein_grams + carbs_grams
calories_per_gram = total_calories / weight_of_food
solids_percentage = 100 - water_percentage
calories = solids_percentage / 100 * calories_per_gram
print(f"{calories :.4f}")
