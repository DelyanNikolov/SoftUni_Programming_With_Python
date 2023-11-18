import re


sentence = input()
searched_word = input()
regex = fr"(?i)\b{searched_word}\b"

result = re.findall(regex, sentence)
print(len(result))
