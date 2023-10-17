def loot_items(action, chest):
    for i in range(1, len(action)):
        if action[i] not in chest:
            chest.insert(0, action[i])


def drop_items(i, chest):
    if 0 <= i < len(chest):
        dropped_item = chest.pop(i)
        chest.append(dropped_item)


def steal_items(count, chest):
    if count > len(chest):
        print(", ".join(chest))
        chest.clear()
        return chest
    else:
        ind = len(chest) - count
        stolen = chest[ind:]
        left = chest[:ind]
        print(", ".join(stolen))
        return left


treasure_chest = input().split("|")

while True:
    command = input().split()
    current_command = command[0]
    if current_command == "Yohoho!":
        break

    elif current_command == "Loot":
        loot_items(command, treasure_chest)
    elif current_command == "Drop":
        index = int(command[1])
        drop_items(index, treasure_chest)
    elif current_command == "Steal":
        count_of_stolen_items = int(command[1])
        treasure_chest = steal_items(count_of_stolen_items, treasure_chest)

if len(treasure_chest) == 0:
    print("Failed treasure hunt.")
else:
    average_gain = sum(len(item) for item in treasure_chest) / len(treasure_chest)
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")
