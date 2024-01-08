string_to_explode = input()
exploded = ""
strength_of_explosion = 0
for index in range(len(string_to_explode)):
    if strength_of_explosion > 0 and string_to_explode[index] != ">":
        strength_of_explosion -= 1
    elif string_to_explode[index] == ">":
        exploded += string_to_explode[index]
        strength_of_explosion += int(string_to_explode[index + 1])
    else:
        exploded += string_to_explode[index]
print(exploded)
