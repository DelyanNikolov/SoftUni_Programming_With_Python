
stadium_capacity = int(input())
fans_count = int(input())

current_fan_sector = ""
fans_in_sector_A = 0
fans_in_sector_B = 0
fans_in_sector_V = 0
fans_in_sector_G = 0

for _ in range(fans_count):
    current_fan_sector = input()
    if current_fan_sector == "A":
        fans_in_sector_A += 1
    elif current_fan_sector == "B":
        fans_in_sector_B += 1
    elif current_fan_sector == "V":
        fans_in_sector_V += 1
    elif current_fan_sector == "G":
        fans_in_sector_G += 1

fans_in_sector_A_percentage = fans_in_sector_A / fans_count * 100
fans_in_sector_B_percentage = fans_in_sector_B / fans_count * 100
fans_in_sector_V_percentage = fans_in_sector_V / fans_count * 100
fans_in_sector_G_percentage = fans_in_sector_G / fans_count * 100
fans_count_percentage = fans_count / stadium_capacity * 100

print(f"{fans_in_sector_A_percentage:.2f}%")
print(f"{fans_in_sector_B_percentage:.2f}%")
print(f"{fans_in_sector_V_percentage:.2f}%")
print(f"{fans_in_sector_G_percentage:.2f}%")
print(f"{fans_count_percentage:.2f}%")
