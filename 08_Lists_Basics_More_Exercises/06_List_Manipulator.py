list_of_numbers = list(map(int, input().split(" ")))

command = input().split(" ")
while "end" not in command:
    if "exchange" in command:
        split_index = int(command[1])
        if split_index > len(list_of_numbers):
            print("Invalid index")
        else:
            left_part = list_of_numbers[:split_index + 1]
            right_part = list_of_numbers[split_index + 1:]
            list_of_numbers.clear()
            list_of_numbers = right_part + left_part

    if "max" in command:
        subcommand = command[1]
        if subcommand == "even":
            even_numbers = [even for even in list_of_numbers if even % 2 == 0]
            if len(even_numbers) < 1:
                print("No matches")
            else:
                max_even_element = max(even_numbers)
                index_of_max_even_element = len(list_of_numbers) - list_of_numbers[:: -1].index(max_even_element) - 1
                print(index_of_max_even_element)
        elif subcommand == "odd":
            odd_numbers = [odd for odd in list_of_numbers if odd % 2 != 0]
            if len(odd_numbers) < 1:
                print("No matches")
            else:
                max_odd_element = max(odd_numbers)
                index_of_max_odd_element = len(list_of_numbers) - list_of_numbers[:: -1].index(max_odd_element) - 1
                print(index_of_max_odd_element)

    if "min" in command:
        subcommand = command[1]
        if subcommand == "even":
            even_numbers = [even for even in list_of_numbers if even % 2 == 0]
            if len(even_numbers) < 1:
                print("No matches")
            else:
                min_even_element = min(even_numbers)
                index_of_min_even_element = len(list_of_numbers) - list_of_numbers[:: -1].index(min_even_element) - 1
                print(index_of_min_even_element)
        elif subcommand == "odd":
            odd_numbers = [odd for odd in list_of_numbers if odd % 2 != 0]
            if len(odd_numbers) < 1:
                print("No matches")
            else:
                min_odd_element = min(odd_numbers)
                index_of_min_odd_element = len(list_of_numbers) - list_of_numbers[:: -1].index(min_odd_element) - 1
                print(index_of_min_odd_element)

    if "first" in command:
        count = int(command[1])
        subcommand = command[2]
        if count > len(list_of_numbers):
            print("Invalid count")
        else:
            if subcommand == "even":
                even_numbers = [even for even in list_of_numbers if even % 2 == 0]
                first_even_numbers = even_numbers[:count]
                print(first_even_numbers)
            elif subcommand == "odd":
                odd_numbers = [odd for odd in list_of_numbers if odd % 2 != 0]
                first_odd_numbers = odd_numbers[:count]
                print(first_odd_numbers)

    if "last" in command:
        count = int(command[1])
        subcommand = command[2]
        if count > len(list_of_numbers):
            print("Invalid count")
        else:
            if subcommand == "even":
                even_numbers = [even for even in list_of_numbers if even % 2 == 0]
                even_numbers = even_numbers[::-1]
                last_even_numbers = even_numbers[:count]
                print(last_even_numbers)
            elif subcommand == "odd":
                odd_numbers = [odd for odd in list_of_numbers if odd % 2 != 0]
                odd_numbers = odd_numbers[::-1]
                last_odd_numbers = odd_numbers[:count]
                print(last_odd_numbers)
    command = input().split(" ")

print(list_of_numbers)
