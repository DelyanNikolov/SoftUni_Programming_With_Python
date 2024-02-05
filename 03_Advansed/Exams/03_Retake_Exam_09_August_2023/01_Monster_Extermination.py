from collections import deque

monsters_armor = deque(int(x) for x in input().split(","))
soldier_impact = [int(x) for x in input().split(",")]

killed_monsters = 0

while monsters_armor and soldier_impact:
    monster = monsters_armor.popleft()
    impact = soldier_impact.pop()

    if impact >= monster:
        impact = impact - monster
        killed_monsters += 1
        if impact > 0 and soldier_impact:
            soldier_impact[-1] += impact
        elif impact > 0 and not soldier_impact:
            soldier_impact.append(impact)
    else:
        monster = monster - impact
        if monster > 0:
            monsters_armor.append(monster)

if not monsters_armor:
    print("All monsters have been killed!")
if not soldier_impact:
    print("The soldier has been defeated.")
print(f"Total monsters killed: {killed_monsters}")
