quantity = int(input())
days = int(input())
ornaments_price = 2
ornaments_spirit = 5
tree_skirt_price = 5
tree_skirt_spirit = 3
tree_garland_price = 3
tree_garland_spirit = 10
tree_lights_price = 15
tree_lights_spirit = 17
expense = 0
spirit = 0

for day in range(1, days + 1):
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        expense += quantity * ornaments_price
        spirit += ornaments_spirit
    if day % 3 == 0:
        expense += quantity * (tree_skirt_price + tree_garland_price)
        spirit += (tree_skirt_spirit + tree_garland_spirit)
    if day % 5 == 0:
        expense += quantity * tree_lights_price
        spirit += tree_lights_spirit
        if day % 3 == 0:
            spirit += 30
    if day % 10 == 0:
        expense += tree_skirt_price + tree_lights_price + tree_garland_price
        spirit -= 20
if days % 10 == 0:
    spirit -= 30

print(f"Total cost: {expense}")
print(f"Total spirit: {spirit}")
