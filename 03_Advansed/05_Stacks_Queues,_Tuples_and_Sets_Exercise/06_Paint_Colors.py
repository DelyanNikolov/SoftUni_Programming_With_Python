from collections import deque

colors = {"red", "yellow", "blue", "orange", "purple", "green"}
secondary_colors = {
    "orange": {"red","yellow"},
    "purple": {"red", "blue"},
    "green": {"yellow","blue"}
}

found_colors = []

some_text = deque(word for word in input().split())

while some_text:
    first_string = some_text.popleft()
    last_string = some_text.pop() if some_text else ""

    for color in (first_string + last_string, last_string + first_string):
        if color in colors:
            found_colors.append(color)
            break
    else:
        for el in (first_string[:-1], last_string[:-1]):
            if el:
                some_text.insert(len(some_text) // 2, el)

for color in set(secondary_colors.keys()).intersection(found_colors):
    if not secondary_colors[color].issubset(found_colors):
        found_colors.remove(color)

print(found_colors)
