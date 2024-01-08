def add_force_user(data: list):
    force_side = data[0]
    force_user = data[1]
    user_found = False
    for user_info in force_users.values():
        if force_user in user_info:
            user_found = True
            break
    if not user_found:
        if force_side not in force_users.keys():
            force_users[force_side] = []
            force_users[force_side].append(force_user)
        else:
            force_users[force_side].append(force_user)


def change_side(data: list):
    force_side = data[1]
    force_user = data[0]
    for user_info in force_users.values():
        if force_user in user_info:
            user_info.remove(force_user)
            break
    if force_side not in force_users.keys():
        force_users[force_side] = []
        force_users[force_side].append(force_user)
    else:
        force_users[force_side].append(force_user)
    print(f"{force_user} joins the {force_side} side!")


force_users = {}
while True:
    command = input()
    if command == "Lumpawaroo":
        break
    if "|" in command:
        input_info = command.split(" | ")
        add_force_user(input_info)
    elif "->" in command:
        input_info = command.split(" -> ")
        change_side(input_info)
for side, users in force_users.items():
    if force_users[side]:
        force_users_count = len(force_users[side])
        print(f"Side: {side}, Members: {force_users_count}")
        for user in users:
            print(f"! {user}")
