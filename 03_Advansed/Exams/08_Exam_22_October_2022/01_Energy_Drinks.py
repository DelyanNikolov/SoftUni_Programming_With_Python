from collections import deque

MAX_CAFFEINE_INTAKE = 300

caffeine_stack = [int(x) for x in input().split(", ")]
energy_drinks = deque([int(y) for y in input().split(", ")])

stamat_caffeine_level = 0

while caffeine_stack and energy_drinks:

    caffeine = caffeine_stack[-1]
    energy_drink = energy_drinks[0]

    current_caffeine_level = caffeine * energy_drink

    if current_caffeine_level + stamat_caffeine_level <= MAX_CAFFEINE_INTAKE:
        stamat_caffeine_level += current_caffeine_level
        caffeine_stack.pop()
        energy_drinks.popleft()
    else:
        caffeine_stack.pop()
        energy_drinks.rotate(-1)
        stamat_caffeine_level -= 30
        if stamat_caffeine_level < 0:
            stamat_caffeine_level = 0

if energy_drinks:
    print(f"Drinks left: { ', '.join(map(str, energy_drinks))}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {stamat_caffeine_level} mg caffeine.")
