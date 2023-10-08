def characters_in_range(char1, char2):
    chars_list = []
    for code in range(ord(char1)+ 1, ord(char2)):
        chars_list.append(chr(code))
    return chars_list


first_character = input()
second_character = input()

final_list = characters_in_range(first_character, second_character)
print(" ".join(final_list))
