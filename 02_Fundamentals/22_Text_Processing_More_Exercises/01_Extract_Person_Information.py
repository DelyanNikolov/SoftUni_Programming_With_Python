number_of_lines = int(input())

for line in range(number_of_lines):
    line_text = input()
    name = line_text[line_text.index("@") + 1:line_text.index("|")]
    age = line_text[line_text.index("#") + 1:line_text.index("*")]
    print(f"{name} is {age} years old.")
