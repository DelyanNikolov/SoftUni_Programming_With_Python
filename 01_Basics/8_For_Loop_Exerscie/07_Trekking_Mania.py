
groups_count = int(input())
musala_people = 0
montblan_people = 0
kilimanjaro_people = 0
k2_people = 0
everest_people = 0
total_people = 0
for _ in range(groups_count):
    people_in_groups = int(input())
    if people_in_groups <= 5:
        musala_people += people_in_groups
    elif people_in_groups <= 12:
        montblan_people += people_in_groups
    elif people_in_groups <= 25:
        kilimanjaro_people += people_in_groups
    elif people_in_groups <= 40:
        k2_people += people_in_groups
    elif people_in_groups > 40:
        everest_people += people_in_groups

total_people = musala_people + montblan_people + kilimanjaro_people + k2_people + everest_people

musala_percentage = musala_people / total_people * 100
montblan_percentage = montblan_people / total_people * 100
kilimanjaro_percentage = kilimanjaro_people / total_people * 100
k2_percentage = k2_people / total_people * 100
everest_percentage = everest_people / total_people * 100

print(f"{musala_percentage:.2f}%")
print(f"{montblan_percentage:.2f}%")
print(f"{kilimanjaro_percentage:.2f}%")
print(f"{k2_percentage:.2f}%")
print(f"{everest_percentage:.2f}%")
