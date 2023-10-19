def fire(index, damage_points, ship):
    if 0 <= index < len(ship):
        ship[index] -= damage_points
        if ship[index] <= 0:
            print("You won! The enemy ship has sunken.")
            exit()


def defend(start_index, end_index, damage_points, ship):
    if 0 <= start_index < len(ship) and 0 <= end_index < len(ship):
        for index in range(start_index, end_index + 1):
            ship[index] -= damage_points
            if ship[index] <= 0:
                print("You lost! The pirate ship has sunken.")
                exit()


def repair(index, amount, ship, max_health):
    if 0 <= index < len(ship):
        heal = min(ship[index] + amount, max_health)
        ship[index] = heal


def print_status(ship, max_health):
    sections_count = sum([1 for section in ship if section < 0.2 * max_health])
    print(f"{sections_count} sections need repair.")


pirate_ship = [int(section) for section in input().split(">")]
battle_ship = [int(section) for section in input().split(">")]
maximum_health_capacity = int(input())

while True:
    command = input().split()

    if command[0] == "Retire":
        break
    elif command[0] == "Fire":
        section_index = int(command[1])
        damage = int(command[2])
        fire(section_index, damage, battle_ship)
    elif command[0] == "Defend":
        begin_index = int(command[1])
        final_index = int(command[2])
        damage = int(command[3])
        defend(begin_index, final_index, damage, pirate_ship)
    elif command[0] == "Repair":
        section_index = int(command[1])
        health = int(command[2])
        repair(section_index, health, pirate_ship, maximum_health_capacity)
    elif command[0] == "Status":
        print_status(pirate_ship, maximum_health_capacity)

pirate_ship_sum = sum(pirate_ship)
battleship_sum = sum(battle_ship)
print(f"Pirate ship status: {pirate_ship_sum}")
print(f"Warship status: {battleship_sum}")
