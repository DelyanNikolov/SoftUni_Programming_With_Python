from collections import deque

materials = [int(x) for x in input().split()]
magic_levels = deque([int(m) for m in input().split()])

crafted_gifts = {}

while materials and magic_levels:
    crafted_gift = ""
    current_material = materials.pop()
    current_magic = magic_levels.popleft()

    result = current_material + current_magic

    if result < 100:
        if result % 2 == 0:
            current_material *= 2
            current_magic *= 3
            result = current_material + current_magic
        else:
            result *= 2

    elif result > 499:
        result /= 2

    if 100 <= result < 200:
        crafted_gift = "Gemstone"
    elif 200 <= result < 300:
        crafted_gift = "Porcelain Sculpture"
    elif 300 <= result < 400:
        crafted_gift = "Gold"
    elif 300 <= result < 500:
        crafted_gift = "Diamond Jewellery"

    if crafted_gift:
        if crafted_gift not in crafted_gifts:
            crafted_gifts[crafted_gift] = 1
        else:
            crafted_gifts[crafted_gift] += 1

if ("Gemstone" in crafted_gifts.keys() and "Porcelain Sculpture" in crafted_gifts.keys())\
        or ("Gold" in crafted_gifts.keys() and "Diamond Jewellery" in crafted_gifts.keys()):
    print(f"The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join(map(str, materials))}")
if magic_levels:
    print(f"Magic left: {', '.join(map(str, magic_levels))}")

for gift, count in sorted(crafted_gifts.items(), key=lambda x: x[0]):
    print(f"{gift}: {count}")
