lost_fights_count = int(input())

helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())


helmets_broken = lost_fights_count // 2
swords_broken = lost_fights_count // 3
shields_brakes = lost_fights_count // (2 + 3)
armors_broken = shields_brakes // 2
# for fight in range(1, lost_fights_count + 1):
#     if fight % 2 == 0:
#         helmets_broken += 1
#
#     if fight % 3 == 0:
#         swords_broken += 1
#
#     if fight % 2 == 0 and fight % 3 == 0:
#         shields_brakes += 1
#
#         if shields_brakes % 2 == 0:
#             armors_broken += 1

total_cost = helmets_broken * helmet_price \
             + swords_broken * sword_price \
             + shields_brakes * shield_price \
             + armors_broken * armor_price
print(f"Gladiator expenses: {total_cost:.2f} aureus")
