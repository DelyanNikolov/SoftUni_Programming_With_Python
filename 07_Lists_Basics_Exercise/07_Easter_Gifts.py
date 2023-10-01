gifts_list = input().split()

command = input()
while command != "No Money":
    if "OutOfStock" in command:
        list_command = command.split()
        gift = list_command[1]
        for i in range(len(gifts_list)):
            if gifts_list[i] == gift:
                gifts_list[i] = "None"
    elif "Required" in command:
        list_command = command.split()
        gift = list_command[1]
        gift_index = int(list_command[2])
        if 0 < gift_index < len(gifts_list):
            gifts_list[gift_index] = gift
    elif "JustInCase" in command:
        list_command = command.split()
        gift = list_command[1]
        gifts_list[-1] = gift
    command = input()
for j in range(len(gifts_list) - 1, -1, -1):
    if gifts_list[j] == "None":
        gifts_list.remove(gifts_list[j])
gifts_to_print = " ".join(gifts_list)
print(gifts_to_print)
