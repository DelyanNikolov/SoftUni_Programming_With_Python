some_string = input().split()
text_to_check = "".join(some_string)
characters = {}
for char in text_to_check:
    if char not in characters:
        characters[char] = 1
    else:
        characters[char] += 1

for item, count in characters.items():
    print(f"{item} -> {count}")
