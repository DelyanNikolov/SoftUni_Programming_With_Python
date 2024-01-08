import re

number_of_strings = int(input())

regex = r"!([A-Z][a-z]{2,})!:\[([A-Za-z]{8,})\]"

for string in range(number_of_strings):
    string_to_check = input()
    is_string_valid = re.findall(regex, string_to_check)
    if is_string_valid:
        translated_string = []
        for item in is_string_valid:
            string_to_translate = item[1]
            for letter in string_to_translate:
                translated_string.append(str(ord(letter)))
            print(f"{item[0]}: {' '.join(translated_string)}")
    else:
        print("The message is invalid")
