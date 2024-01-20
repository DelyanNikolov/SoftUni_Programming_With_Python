from collections import deque

presents = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
}

crafted_presents = []

materials = [int(m) for m in input().split()]
magic_levels = deque(int(m) for m in input().split())

while materials and magic_levels:
    # material = materials.pop()
    # magic = magic_levels.popleft()
    #
    # if not material and not magic:
    #     continue
    # elif not material:
    #     magic_levels.appendleft(magic)
    #     continue
    # elif not magic:
    #     materials.append(material)
    #     continue
    material = materials.pop() if magic_levels[0] or not materials[-1] else 0
    magic = magic_levels.popleft() if material or not magic_levels[0] else 0
    if not magic:
        continue

    magic_level = material * magic

    if presents.get(magic_level):
        crafted_presents.append(presents[magic_level])
    elif magic_level < 0:
        materials.append(material + magic)
    elif magic_level > 0:
        materials.append(material + 15)

if {"Doll", "Wooden train"}.issubset(crafted_presents) or {"Teddy bear", "Bicycle"}.issubset(crafted_presents):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials)}")
if magic_levels:
    print(f"Magic left: {', '.join(str(x) for x in magic_levels)}")

[print(f"{toy}: {crafted_presents.count(toy)}") for toy in sorted(set(crafted_presents))]
