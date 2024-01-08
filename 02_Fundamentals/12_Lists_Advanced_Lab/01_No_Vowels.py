some_string = input()

sorted_string = [letter for letter in some_string if letter.lower() not in ['a', 'o', 'u', 'e', 'i']]

print("".join(sorted_string))
