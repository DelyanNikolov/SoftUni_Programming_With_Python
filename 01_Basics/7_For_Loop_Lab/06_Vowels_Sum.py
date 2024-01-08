some_string = input()

total_points = 0

for character in some_string:
    if character == "a":
        total_points += 1
    elif character == "e":
        total_points += 2
    elif character == "i":
        total_points += 3
    elif character == "o":
        total_points += 4
    elif character == "u":
        total_points += 5

print(total_points)
