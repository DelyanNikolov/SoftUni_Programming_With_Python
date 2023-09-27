n = int(input())
special_word = input()
strings = []
for _ in range(n):
    current_string = input()
    strings.append(current_string)
print(strings)

for i in range(len(strings) - 1, -1, -1):
    element = strings[i]
    if special_word not in element:
        strings.remove(element)
print(strings)