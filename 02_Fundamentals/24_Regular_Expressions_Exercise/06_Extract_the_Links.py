import re


line = input()
pattern = r"(www\.[a-zA-Z0-9\-\.]+\.{1}[a-z]+)"
while line:
    match = re.search(pattern, line)
    if match:
        valid_url = match.group(1)
        print(valid_url)
    line = input()