heroes_count = int(input())
maximum_health = 100
maximum_mana = 200


def get_hero_info(name, hp, mp):
    return {name: {"health": hp, "mana": mp}}


def cast_spell_action(name, mp, spell):
    for hero in heroes_stats:
        if name in hero.keys():
            if hero[name]['mana'] >= mp:
                hero[name]['mana'] -= mp
                print(f"{name} has successfully cast {spell} and now has {hero[name]['mana']} MP!")
            else:
                print(f"{name} does not have enough MP to cast {spell}!")


def take_damage_action(name, points, attacker):
    for hero in heroes_stats:
        if name in hero.keys():
            hero[name]['health'] -= points
            if hero[name]['health'] > 0:
                print(f"{name} was hit for {points} HP by {attacker} and now has {hero[name]['health']} HP left!")
            else:
                print(f"{name} has been killed by {attacker}!")
                del hero[name]


def recharge_action(name, points):
    for hero in heroes_stats:
        if name in hero.keys():
            amount = min(maximum_mana - hero[name]['mana'], points)
            hero[name]['mana'] += amount
            print(f"{name} recharged for {amount} MP!")


def heal_action(name, points):
    for hero in heroes_stats:
        if name in hero.keys():
            amount = min(maximum_health - hero[name]['health'], points)
            hero[name]['health'] += amount
            print(f"{name} healed for {amount} HP!")


heroes_stats = []
for _ in range(heroes_count):
    hero_data = input().split()
    hero_name = hero_data[0]
    hero_health = int(hero_data[1])
    hero_mana = int(hero_data[2])
    heroes_stats.append(get_hero_info(hero_name, hero_health, hero_mana))

while True:
    command = input().split(" - ")
    action = command[0]
    if action == "End":
        break
    elif action == "CastSpell":
        hero_name, mp_needed, spell_name = command[1], int(command[2]), command[3]
        cast_spell_action(hero_name, mp_needed, spell_name)
    elif action == "TakeDamage":
        hero_name, damage_points, attacker_name = command[1], int(command[2]), command[3]
        take_damage_action(hero_name, damage_points, attacker_name)
    elif action == "Recharge":
        hero_name, recharge_amount = command[1], int(command[2])
        recharge_action(hero_name, recharge_amount)
    elif action == "Heal":
        hero_name, heal_amount = command[1], int(command[2])
        heal_action(hero_name, heal_amount)

for hero_left in heroes_stats:
    for h_name, stat in hero_left.items():
        print(h_name)
        print(f"  HP: {stat['health']}")
        print(f"  MP: {stat['mana']}")
