zoo_data = {}
zoo_areas = {}
while True:
    command = input().split(": ")
    if command[0] == "EndDay":
        break
    elif command[0] == "Add":
        animal_info = command[1].split("-")
        name_of_animal = animal_info[0]
        needed_food = int(animal_info[1])
        area_name = animal_info[2]
        if name_of_animal in zoo_data:
            zoo_data[name_of_animal]["needed_food"] += needed_food
        else:
            zoo_data[name_of_animal] = {"needed_food": needed_food, "area": area_name}

    elif command[0] == "Feed":
        animal_info = command[1].split("-")
        name_of_animal = animal_info[0]
        food_fed = int(animal_info[1])
        if name_of_animal not in zoo_data:
            continue
        zoo_data[name_of_animal]["needed_food"] -= food_fed
        if zoo_data[name_of_animal]["needed_food"] <= 0:
            print(f"{name_of_animal} was successfully fed")
            zoo_data.pop(name_of_animal)

print("Animals:")
for name, info in zoo_data.items():
    print(f" {name} -> {info['needed_food']}g")
    if info["area"] not in zoo_areas:
        zoo_areas[info["area"]] = []
    zoo_areas[info["area"]].append(name)
print("Areas with hungry animals:")
for zone, animals in zoo_areas.items():
    print(f" {zone}: {len(animals)}")
