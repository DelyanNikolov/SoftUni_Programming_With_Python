quantity_food = float(input())
quantity_hay = float(input())
quantity_cover = float(input())
guinea_pig_weight = float(input())

days = 30
for day in range(1, days + 1):
    quantity_food -= 0.3
    if quantity_food <= 0:
        break
    if day % 2 == 0:
        quantity_hay -= 0.05 * quantity_food
        if quantity_hay <= 0:
            break
    if day % 3 == 0:
        quantity_cover -= guinea_pig_weight / 3
        if quantity_cover <= 0:
            break
if round(quantity_food, 2) <= 0 or round(quantity_hay, 2) <= 0 or round(quantity_cover, 2) <= 0:
    print("Merry must go to the pet store!")
else:
    print(f"Everything is fine! Puppy is happy! Food: {quantity_food:.2f}, Hay: {quantity_hay:.2f}, "
          f"Cover: {quantity_cover:.2f}.")
