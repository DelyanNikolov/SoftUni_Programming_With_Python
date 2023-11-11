some_string = input()
string_to_print = ""
current_string = ""
repetitions = ""
for index in range(len(some_string)):
    if not some_string[index].isdigit():
        current_string += some_string[index].upper()
    else:
        for next_numbers in range(index, len(some_string)):
            if not some_string[next_numbers].isdigit():
                break
            repetitions += some_string[next_numbers]
        string_to_print += current_string * int(repetitions)
        current_string = ""
        repetitions = ""
print(f"Unique symbols used: {len(set(string_to_print))}")
print(string_to_print)
