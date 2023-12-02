def pr_msg():
    print(all_stops)


all_stops = input()
while True:
    command = input().split(":")
    if command[0] == "Travel":
        break
    elif command[0] == "Add Stop":
        index = int(command[1])
        string = command[2]
        if index in range(len(all_stops)):
            all_stops = all_stops[:index] + string + all_stops[index:]
    elif command[0] == "Remove Stop":
        start_index = int(command[1])
        end_index = int(command[2])
        if start_index in range(len(all_stops)) and end_index in range(len(all_stops)):
            all_stops = all_stops[:start_index] + all_stops[end_index + 1:]
    elif command[0] == "Switch":
        old_string, new_string = command[1], command[2]
        if old_string in all_stops:
            all_stops = all_stops.replace(old_string, new_string)
    pr_msg()
print(f"Ready for world tour! Planned stops: {all_stops}")
