# You will be given number n. After that,
# you'll receive different strings n times. Your task is to check if the given strings are pure,' \
#    ' meaning that they do NOT consist of any of the characters: comma ",", period ".", or underscore "_":
# •	If a string is pure, print "{string} is pure."
# •	Otherwise, print "{string} is not pure!"

strings_count = int(input())

for _ in range(strings_count):
    string = input()
    for char in string:
        if char == "," or char == "." or char == "_":
            print(f"{string} is not pure!")
            break
    else:
        print(f"{string} is pure.")
