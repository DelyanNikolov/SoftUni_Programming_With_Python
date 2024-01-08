raw_activation_key = input()
raw_activation_key_list = [char for char in raw_activation_key]

command = input()
while command != "Generate":
    if "Contains" in command:
        substring = command.split(">>>")[1]
        string_to_check = "".join(raw_activation_key_list)
        if substring in string_to_check:
            print(f"{string_to_check} contains {substring}")
        else:
            print(f"Substring not found!")
    elif "Flip" in command:
        line = command.split(">>>")
        case = line[1]
        start_index = int(line[2])
        end_index = int(line[3])
        key_to_print = ""
        if case == "Upper":
            for index in range(start_index, end_index):
                raw_activation_key_list[index] = raw_activation_key_list[index].upper()
            key_to_print = "".join(raw_activation_key_list)
            print(key_to_print)
        elif case == "Lower":
            for index in range(start_index, end_index):
                raw_activation_key_list[index] = raw_activation_key_list[index].lower()
            key_to_print = "".join(raw_activation_key_list)
            print(key_to_print)
    elif "Slice" in command:
        line = command.split(">>>")
        start_index = int(line[1])
        end_index = int(line[2])
        del raw_activation_key_list[start_index: end_index]
        key_to_print = "".join(raw_activation_key_list)
        print(key_to_print)
    command = input()
print(f"Your activation key is: {''.join(raw_activation_key_list)}")
