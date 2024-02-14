from collections import deque

firework_effects_que = deque([int(f) for f in input().split(", ")])
explosive_powers_stack = [int(e) for e in input().split(", ")]

palm_firework_count = 0
willow_firework = 0
crossette_firework = 0

perfect_show = False

while firework_effects_que and explosive_powers_stack:

    if firework_effects_que[0] <= 0:
        firework_effects_que.popleft()
        continue
    if explosive_powers_stack[-1] <= 0:
        explosive_powers_stack.pop()
        continue

    effect = firework_effects_que.popleft()
    power = explosive_powers_stack.pop()

    result = effect + power

    if result % 3 == 0 and result % 5 == 0:
        crossette_firework += 1
    elif result % 3 == 0 and result % 5 != 0:
        palm_firework_count += 1
    elif result % 3 != 0 and result % 5 == 0:
        willow_firework += 1
    else:
        effect -= 1
        firework_effects_que.append(effect)
        explosive_powers_stack.append(power)

    if palm_firework_count >= 3 and willow_firework >= 3 and crossette_firework >= 3:
        perfect_show = True
        break

if perfect_show:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if firework_effects_que:
    print(f"Firework Effects left: {', '.join(map(str, firework_effects_que))}")
if explosive_powers_stack:
    print(f"Explosive Power left: {', '.join(map(str, explosive_powers_stack))}")

print(f"Palm Fireworks: {palm_firework_count}")
print(f"Willow Fireworks: {willow_firework}")
print(f"Crossette Fireworks: {crossette_firework}")
