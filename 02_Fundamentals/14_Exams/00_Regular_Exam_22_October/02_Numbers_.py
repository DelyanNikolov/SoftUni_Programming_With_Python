list_of_numbers = [int(num) for num in input().split()]

command = input().split()
while not command[0] == "Finish":
    if command[0] == "Add":
        value = int(command[1])
        list_of_numbers.append(value)
    elif command[0] == "Remove":
        value = int(command[1])
        if value in list_of_numbers:
            list_of_numbers.remove(value)
    elif command[0] == "Replace":
        value = int(command[1])
        replacement_value = int(command[2])
        if value in list_of_numbers:
            value_index = list_of_numbers.index(value)
            list_of_numbers[value_index] = replacement_value
    elif command[0] == "Collapse":
        compare_value = int(command[1])
        list_of_numbers = [num for num in list_of_numbers if num >= compare_value]
    command = input().split()
print(" ".join(map(str, list_of_numbers)))
