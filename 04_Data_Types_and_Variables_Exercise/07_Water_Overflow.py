water_tank_capacity = 255

num_of_fills = int(input())
full_space = 0
empty_space = 255
for fill in range(num_of_fills):
    litters_of_water = int(input())
    if litters_of_water <= empty_space:
        full_space += litters_of_water
        empty_space -= litters_of_water
    else:
        print("Insufficient capacity!")
        continue
print(full_space)

