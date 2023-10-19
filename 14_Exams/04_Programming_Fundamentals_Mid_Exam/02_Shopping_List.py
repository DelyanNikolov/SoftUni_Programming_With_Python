list_of_groceries = input().split("!")

while True:
    action = input().split()
    command = action[0]
    if action[0] == "Go" and action[1] == "Shopping!":
        break
    elif command == "Urgent":
        item = action[1]
        if item not in list_of_groceries:
            list_of_groceries.insert(0, item)
    elif command == "Unnecessary":
        item = action[1]
        if item in list_of_groceries:
            list_of_groceries.remove(item)
    elif command == "Correct":
        old_item = action[1]
        new_item = action[2]
        if old_item in list_of_groceries:
            old_item_index = list_of_groceries.index(old_item)
            list_of_groceries.pop(old_item_index)
            list_of_groceries.insert(old_item_index, new_item)
    elif command == "Rearrange":
        item = action[1]
        if item in list_of_groceries:
            list_of_groceries.remove(item)
            list_of_groceries.append(item)

print(", ".join(list_of_groceries))
