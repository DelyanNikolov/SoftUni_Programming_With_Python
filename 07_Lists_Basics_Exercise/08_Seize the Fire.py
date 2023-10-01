level_of_fire = input().split("#")
amount_of_water = int(input())

cells = []
effort = 0
total_fire = 0

for fire in range(len(level_of_fire)):
    is_fire_valid = True
    data = level_of_fire[fire].split(" = ")
    fire_type = data[0]
    fire_range = int(data[1])
    if amount_of_water < 0:
        break
    if amount_of_water < fire_range:
        continue
    if fire_type == "High" and not 81 <= fire_range <= 125:
        is_fire_valid = False
    elif fire_type == "Medium" and not 51 <= fire_range <= 80:
        is_fire_valid = False
    elif fire_type == "Low" and not 1 <= fire_range <= 50:
        is_fire_valid = False
    if not is_fire_valid:
        continue
    else:
        cells.append(fire_range)
        amount_of_water -= fire_range
        total_fire += fire_range
        effort += 0.25 * fire_range
print("Cells:")
for item in cells:
    print(f" - {item}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
