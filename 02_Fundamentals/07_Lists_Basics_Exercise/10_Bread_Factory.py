energy = 100
coins = 100
day_completed = True
working_day_events = input().split("|")

for event_index in range(len(working_day_events)):
    event_data = working_day_events[event_index].split("-")
    event_name = event_data[0]
    event_value = int(event_data[1])

    if event_name == "rest":
        if energy == 100:
            gained_energy = 0
        elif energy + event_value > 100:
            gained_energy = 100 - energy
        else:
            gained_energy = event_value
        energy += gained_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")
    elif event_name == "order":

        if energy < 30:
            energy += 50
            if energy > 100:
                energy = 100
            print("You had to rest!")
        else:
            energy -= 30
            coins += event_value
            print(f"You earned {event_value} coins.")
    else:
        ingredient = event_name
        if coins >= event_value:
            coins -= event_value
            print(f"You bought {ingredient}.")
        else:
            print(f"Closed! Cannot afford {ingredient}.")
            day_completed = False
            break
if day_completed:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
