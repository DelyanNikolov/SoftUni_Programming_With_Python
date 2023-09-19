# You will be given strings until you receive the command "End". For each string given,
# you should print a string in which each character (case-sensitive) is repeated twice.
# Note that if you receive the string "SoftUni", you should NOT print it!

while True:
    command = input()
    if command == "End":
        break
    string = command
    if string == "SoftUni":
        continue
    new_string = ""
    for character in string:
        new_string += character + character
    print(new_string)
