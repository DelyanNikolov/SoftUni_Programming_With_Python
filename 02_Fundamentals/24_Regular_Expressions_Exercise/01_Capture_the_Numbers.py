import re


regex = r"\d+"

while True:
    some_text = input()
    if not some_text:
        break
    matches = re.findall(regex, some_text)
    if matches:
        print(" ".join(matches), end=" ")
