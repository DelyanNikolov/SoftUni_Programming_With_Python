single_string = input()
result = ""
current_char = ""
for char in single_string:
    if char != current_char:
        result += char
        current_char = char

print(result)
