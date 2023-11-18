import re

some_text = input()
regex = r"\b_([A-Za-z0-9]+)\b"
result = re.findall(regex, some_text)

print(",".join(result))
