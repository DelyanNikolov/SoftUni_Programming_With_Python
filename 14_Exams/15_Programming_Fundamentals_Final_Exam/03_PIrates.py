cities_data = {}
while True:
    command = input()
    if command == "Sail":
        break
    cities_info = command.split("||")
    name = cities_info[0]
    population = int(cities_info[1])
    gold = int(cities_info[2])

    if name not in cities_data.keys():
        cities_data[name] = {"population": 0, "gold": 0}
    if name in cities_data.keys():
        cities_data[name]["population"] += population
        cities_data[name]["gold"] += gold

while True:
    command = input().split("=>")
    if command[0] == "End":
        break

    if command[0] == "Plunder":
        town_name = command[1]
        people_killed = int(command[2])
        gold_taken = int(command[3])

        cities_data[town_name]["population"] -= people_killed
        cities_data[town_name]["gold"] -= gold_taken
        print(f"{town_name} plundered! {gold_taken} gold stolen, {people_killed} citizens killed.")

        if cities_data[town_name]["population"] <= 0 or cities_data[town_name]["gold"] <= 0:
            print(f"{town_name} has been wiped off the map!")
            del cities_data[town_name]
    elif command[0] == "Prosper":
        town_name = command[1]
        gold_added = int(command[2])
        if gold_added < 0:
            print("Gold added cannot be a negative number!")
            continue
        else:
            cities_data[town_name]["gold"] += gold_added
            print(f"{gold_added} gold added to the city treasury. {town_name} now has {cities_data[town_name]['gold']} gold.")

if len(cities_data) > 0:
    print(f"Ahoy, Captain! There are {len(cities_data.keys())} wealthy settlements to go to:")
    for town, info in cities_data.items():
        print(f"{town} -> Population: {info['population']} citizens, Gold: {info['gold']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
