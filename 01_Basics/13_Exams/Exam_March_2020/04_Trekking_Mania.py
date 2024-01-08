climbers_count = 0
mousala = 0
montblanc = 0
kilimanjaro = 0
k_2 = 0
everest = 0
groups_count = int(input())
for _ in range(groups_count):
    current_climbers = int(input())
    climbers_count += current_climbers
    if current_climbers <= 5:
        mousala += current_climbers
    elif current_climbers <= 12:
        montblanc += current_climbers
    elif current_climbers <= 25:
        kilimanjaro += current_climbers
    elif current_climbers <= 40:
        k_2 += current_climbers
    elif current_climbers > 40:
        everest += current_climbers
mousala_percentage = mousala / climbers_count * 100
montblanc_percentage = montblanc / climbers_count * 100
kilimanjaro_percentage = kilimanjaro / climbers_count * 100
k2_percentage = k_2 / climbers_count * 100
everest_percentage = everest / climbers_count * 100

print(f"{mousala_percentage :.2f}%")
print(f"{montblanc_percentage :.2f}%")
print(f"{kilimanjaro_percentage :.2f}%")
print(f"{k2_percentage :.2f}%")
print(f"{everest_percentage :.2f}%")
