health = 100
bitcoins = 0

dungeon_rooms = input().split("|")
best_room = 0
is_dead = False
for room in dungeon_rooms:
    best_room += 1
    action = room.split()
    command = action[0]

    if command == "potion":
        heal_amount = int(action[1])
        current_health = health
        health = min((health + heal_amount), 100)
        amount = health - current_health
        print(f"You healed for {amount} hp.")
        print(f"Current health: {health} hp.")

    elif command == "chest":
        amount = int(action[1])
        bitcoins += amount
        print(f"You found {amount} bitcoins.")

    else:
        monster = action[0]
        monster_attack = int(action[1])
        health -= monster_attack
        if health <= 0:
            print(f"You died! Killed by {monster}.")
            print(f"Best room: {best_room}")
            is_dead = True
            break
        else:
            print(f"You slayed {monster}.")

if not is_dead:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
