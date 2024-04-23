def collect_dwarfs_info():
    global dwarfs_list
    # separating dwarfs info from the input
    while True:
        command = input().split(" <:> ")
        if command[0] == "Once upon a time":
            break
        dwarf_name = command[0]
        dwarf_hat_color = command[1]
        dwarf_physics = int(command[2])
        new_dwarf = {
            "name": dwarf_name,
            "hat_colour": dwarf_hat_color,
            "dwarf_physics": dwarf_physics
        }

        # check for:
        # If 2 dwarfs have the same name but different colors, they should be considered different dwarfs,
        # and you should store them both.
        # f 2 dwarfs have the same name and the same color, store the one with the higher physics.
        if new_dwarf["hat_colour"] not in dwarfs_list:
            dwarfs_list[dwarf_hat_color] = {}
            if new_dwarf["name"] not in dwarfs_list[dwarf_hat_color]:
                dwarfs_list[dwarf_hat_color][dwarf_name] = dwarf_physics
        else:
            if new_dwarf["name"] in dwarfs_list[dwarf_hat_color] and \
                    new_dwarf["dwarf_physics"] > dwarfs_list[dwarf_hat_color][dwarf_name]:
                dwarfs_list[dwarf_hat_color][dwarf_name] = new_dwarf["dwarf_physics"]
            else:
                dwarfs_list[dwarf_hat_color][dwarf_name] = dwarf_physics


def display_result(dwarfs_list):
    dwarfs_info = []
    result = []
    for hat_colour in dwarfs_list:
        for name, bmi in dwarfs_list[hat_colour].items():
            dwarfs_info.append({"count": len(hat_colour), "name": name, "BMI": bmi, "hat colour": hat_colour})
    for dwarf in sorted(dwarfs_info, key=lambda d: (-d["BMI"], -d["count"])):
        result.append(f"({dwarf['hat colour']}) {dwarf['name']} <-> {dwarf['BMI']}")

    print('\n'.join(result))


dwarfs_list = {}

collect_dwarfs_info()
display_result(dwarfs_list)
