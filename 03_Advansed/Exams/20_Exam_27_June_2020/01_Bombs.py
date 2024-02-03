from collections import deque


def check_is_pouch_full():
    full = False
    for item in pouch:
        if pouch[item] >= 3:
            full = True
        else:
            full = False
            break
    return full


bombs = {40: "Datura Bombs",
         60: "Cherry Bombs",
         120: "Smoke Decoy Bombs"
         }

pouch = {
    "Datura Bombs": 0,
    "Cherry Bombs": 0,
    "Smoke Decoy Bombs": 0
}

bomb_effects = deque(int(x) for x in input().split(", "))
bomb_casings = [int(c) for c in input().split(", ")]

while bomb_effects and bomb_casings:
    effect = bomb_effects.popleft()
    casing = bomb_casings.pop()
    sum_of_materials = effect + casing
    if sum_of_materials in bombs.keys():
        bomb_name = bombs[sum_of_materials]
        pouch[bomb_name] += 1
        if check_is_pouch_full():
            break
    else:
        casing -= 5
        bomb_effects.appendleft(effect)
        bomb_casings.append(casing)

if check_is_pouch_full():
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if not bomb_effects:
    print("Bomb Effects: empty")
else:
    print(f"Bomb Effects: {', '.join([str(b) for b in bomb_effects])}")

if not bomb_casings:
    print("Bomb Casings: empty")
else:
    print(f"Bomb Casings: {', '.join([str(b) for b in bomb_casings])}")

for name, quantity in sorted(pouch.items()):
    print(f"{name}: {quantity}")
