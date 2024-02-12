from collections import deque

elfs_energy_que = deque([int(x) for x in input().split()])
boxes_with_materials = deque([int(x) for x in input().split()])

total_used_energy = 0
total_number_of_toys = 0
turns_counter = 1

while elfs_energy_que and boxes_with_materials:
    toys_to_add = 0
    energy_to_add = 0

    if elfs_energy_que[0] < 5:
        elfs_energy_que.popleft()
        continue

    current_elf_energy = elfs_energy_que.popleft()
    current_box_materials = boxes_with_materials[-1]

    if turns_counter % 3 == 0:
        current_box_materials *= 2
        toys_to_add += 1

    if current_elf_energy >= current_box_materials:
        energy_to_add += current_box_materials
        current_elf_energy -= current_box_materials
        if turns_counter % 5 != 0:
            current_elf_energy += 1
            toys_to_add += 1
        else:
            toys_to_add = 0

        current_box_materials = boxes_with_materials.pop()
    else:
        current_elf_energy *= 2
        toys_to_add = 0

    total_number_of_toys += toys_to_add
    total_used_energy += energy_to_add
    turns_counter += 1
    elfs_energy_que.append(current_elf_energy)

print(f"Toys: {total_number_of_toys}")
print(f"Energy: {total_used_energy}")
if elfs_energy_que:
    print(f"Elves left: {', '.join(map(str, elfs_energy_que))}")
if boxes_with_materials:
    print(f"Boxes left: {', '.join(map(str, boxes_with_materials))}")
