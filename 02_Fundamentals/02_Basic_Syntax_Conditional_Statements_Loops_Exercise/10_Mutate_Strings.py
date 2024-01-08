# You will be given two strings. Transform the first string into the second one, letter by letter,
# starting from the first one. After each interaction, print the resulting string only if it is unique.
# Note: the strings will have the same length.
str1 = input()
str2 = input()
list1 = list(str1)
list2 = list(str2)
check = ""
for item in range(len(str1)):
    list1[item] = list2[item]
    mutated_string = "".join(list1)
    if mutated_string != check and mutated_string != str1:
        print(mutated_string)
        check = mutated_string
