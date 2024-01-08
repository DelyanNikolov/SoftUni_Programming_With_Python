number_of_lines = int(input())
string_to_check = ""
is_open = False
is_balanced = True
for _ in range(number_of_lines):
    character = input()
    string_to_check += character
    if character == "(" and is_open:
        is_balanced = False
        break
    elif character == ")" and not is_open:
        is_balanced = False
        break
    if character == "(":
        is_open = True
    if character == ")" and is_open:
        is_open = False
        is_balanced = True

if is_balanced:
    print("BALANCED")
else:
    print("UNBALANCED")
