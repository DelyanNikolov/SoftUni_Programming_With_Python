initial_string = input()
numbers_list = [num for num in initial_string if num.isdigit()]
alphabetic_list = [num for num in initial_string if not num.isdigit()]

take_list = []
skip_list = []
for ind in range(len(numbers_list)):
    if ind % 2 == 0:
        take_list.append(numbers_list[ind])
    else:
        skip_list.append(numbers_list[ind])

decoded_message = []
for i in range(len(take_list)):
    take_characters_count = int(take_list[i])
    skip_characters_count = int(skip_list[i])
    decoded_message += alphabetic_list[:take_characters_count]
    alphabetic_list = alphabetic_list[take_characters_count + skip_characters_count:]
    to_decode = decoded_message


print("".join(decoded_message))
