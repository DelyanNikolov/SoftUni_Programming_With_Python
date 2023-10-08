def max_odd(data):
    lst = [x for x in data if x % 2 != 0][-1]
    if len(lst) < 1:
        return "No matches"
    else:
        pass

def max_even(data):
    return sorted([x for x in data if x % 2 == 0])[-1]


def min_odd(data):
    lst = sorted([x for x in data if x % 2 != 0])
    if len(lst) < 1:
        return "No matches"
    else:
        min_odd_element = min(lst)
        index_min_odd_element = data.index(min_odd_element)
        return index_min_odd_element


def min_even(data):
    lst = [x for x in data if x % 2 == 0]
    if len(lst) < 1:
        return "No matches"
    else:
        min_even_element = min(lst)
        index_min_even_element = data.index(min_even_element)
        return index_min_even_element


def first_odd(data, numbers):
    odds = []
    for num in data:
        if num % 2 != 0:
            odds.append(num)
    firs_odds = odds[:numbers]
    return firs_odds


def first_even(data, numbers):
    evens = []
    if numbers > len(data) - 1:
        return "Invalid count"
    else:
        for num in data:
            if num % 2 == 0:
                evens.append(num)
        evens = evens[:numbers]
        return evens


def last_odd(data, numbers):
    last_odds = []
    for num in range((len(data) - 1), -1, -1):
        if data[num] % 2 != 0:
            last_odds.append(data[num])
    last_odds = last_odds[:numbers + 1]
    return last_odds[::-1]


def last_even(data, numbers):
    last_odds = []
    for _ in range(numbers):
        for num in range((len(data) - 1), -1, -1):
            if data[num] % 2 == 0:
                last_odds.append(data[num])
    return last_odds[::-1]


initial_list = input().split()
initial_list = list(map(int, initial_list))
command = input().split()
while "end" not in command:
    if "exchange" in command:
        index = int(command[1])
        if index > len(initial_list) - 1:
            print("Invalid index")
        else:
            left_part = initial_list[:index + 1]
            right_part = initial_list[index + 1:]
            initial_list.clear()
            initial_list = right_part + left_part

    if "max" in command:
        sub_command = command[1]
        if sub_command == "odd":

            max_odd_element = max_odd(initial_list)
            index_max_ood_element = initial_list.index(max_odd_element)
            print(index_max_ood_element)
        elif sub_command == "even":
            max_even_element = max_even(initial_list)
            index_max_even_element = initial_list.index(max_even_element)
            print(index_max_even_element)

    if "min" in command:
        sub_command = command[1]
        if sub_command == "odd":
            print(min_odd(initial_list))
        elif sub_command == "even":
            print(min_even(initial_list))
    if "first" in command:
        count = int(command[1])
        sub_command = command[2]
        if sub_command == "odd":
            print(first_odd(initial_list, count))
        elif sub_command == "even":
            print(first_even(initial_list, count))

    if "last" in command:
        count = int(command[1])
        sub_command = command[2]
        if count > len(initial_list):
            print("Invalid count")
        if sub_command == "odd":
            print(last_odd(initial_list, count))
        elif sub_command == "even":
            print(last_even(initial_list, count))

    command = input().split()
print(initial_list)
