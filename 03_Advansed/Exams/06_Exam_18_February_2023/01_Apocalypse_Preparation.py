from collections import deque

items = {
    30: "Patch",
    40: "Bandage",
    100: "MedKit"
}

textiles = deque([int(t) for t in input().split()])
medicaments = [int(m) for m in input().split()]

created_items = {}

while textiles and medicaments:
    textile = textiles.popleft()
    medicament = medicaments.pop()

    sum_of_materials = textile + medicament

    if sum_of_materials in items.keys():
        item = items[sum_of_materials]
        if item not in created_items:
            created_items[item] = 0
        created_items[item] += 1
    elif sum_of_materials > 100:
        if "MedKit" not in created_items:
            created_items["MedKit"] = 0
        created_items["MedKit"] += 1
        rest_of_materials = sum_of_materials - 100
        medicaments[-1] += rest_of_materials
    else:
        medicament += 10
        medicaments.append(medicament)

if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")
elif not textiles:
    print("Textiles are empty.")
elif not medicaments:
    print("Medicaments are empty.")

for item, count in sorted(created_items.items(), key=lambda kvp: (-kvp[1], kvp[0])):
    print(f"{item} - {count}")

if medicaments:
    medicaments.reverse()
    print(f"Medicaments left: {', '.join(map(str, medicaments))}")
if textiles:
    print(f"Textiles left: {', '.join(map(str, textiles))}")
