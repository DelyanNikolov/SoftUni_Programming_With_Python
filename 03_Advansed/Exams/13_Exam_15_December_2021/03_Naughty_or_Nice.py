def naughty_or_nice_list(santas_list, *commands, **kids):
    result = []
    naughty_list = []
    nice_list = []
    not_found_list = []
    for string in commands:
        matches_found = []
        command = string.split("-")
        num = int(command[0])
        category = command[1]
        for number, name in santas_list:
            if num == number:
                matches_found.append((category, name, number))
        if len(matches_found) > 1 or not matches_found:
            continue
        else:
            if matches_found[0][0] == "Nice":
                nice_list.append(matches_found[0][1])
                santas_list.remove((matches_found[0][2], matches_found[0][1]))
            elif matches_found[0][0] == "Naughty":
                naughty_list.append(matches_found[0][1])
                santas_list.remove((matches_found[0][2], matches_found[0][1]))

    for name, category in kids.items():
        kids_found = []
        for id_kid, kid_name in santas_list:
            if name == kid_name:
                kids_found.append((category, kid_name, id_kid))
        if len(kids_found) > 1 or not kids_found:
            continue
        else:
            if kids_found[0][0] == "Nice":
                nice_list.append(kids_found[0][1])
                santas_list.remove((kids_found[0][2], kids_found[0][1]))
            elif kids_found[0][0] == "Naughty":
                naughty_list.append(kids_found[0][1])
                santas_list.remove((kids_found[0][2], kids_found[0][1]))

    for id_name, name in santas_list:
        not_found_list.append(name)

    if nice_list:
        result.append(f"Nice: {', '.join(nice_list)}")
    if naughty_list:
        result.append(f"Naughty: {', '.join(naughty_list)}")
    if not_found_list:
        result.append(f"Not found: {', '.join(not_found_list)}")

    return '\n'.join(result)


print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))
