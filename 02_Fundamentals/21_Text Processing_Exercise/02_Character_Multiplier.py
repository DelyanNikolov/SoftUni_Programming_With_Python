strings = input().split()
string_1 = strings[0]
string_2 = strings[1]
multiplied_character_sum = 0
if len(string_1) == len(string_2):
    for index in range(len(string_1)):
        multiplied_character_sum += ord(string_1[index]) * ord(string_2[index])

elif len(string_1) < len(string_2):
    for index in range(len(string_1)):
        multiplied_character_sum += ord(string_1[index]) * ord(string_2[index])
    for index in range(len(string_1), len(string_2)):
        multiplied_character_sum += ord(string_2[index])

elif len(string_1) > len(string_2):
    for index in range(len(string_2)):
        multiplied_character_sum += ord(string_1[index]) * ord(string_2[index])
    for index in range(len(string_2), len(string_1)):
        multiplied_character_sum += ord(string_1[index])

print(multiplied_character_sum)
