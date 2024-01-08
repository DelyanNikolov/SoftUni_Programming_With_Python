import re

some_text = input()
mirror_words = {}
regex = r"([#@])([A-Za-z]{3,})(\1){2}([A-Za-z]{3,})(\1)"
matches = re.findall(regex, some_text)
result = []
for match in matches:
    word = match[1]
    mirror = match[3]
    if word == mirror[::-1]:
        mirror_words[word] = mirror

if not matches:
    print("No word pairs found!")
else:
    print(f"{len(matches)} word pairs found!")
if mirror_words:
    for item, value in mirror_words.items():
        result.append(f"{item} <=> {value}")
    print("The mirror words are:")
    print(", ".join(result))
else:
    print("No mirror words!")
