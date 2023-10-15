first_strings = input().split(", ")
second_strings = input().split()

new_list = []

for word in first_strings:
    for search_word in second_strings:
        if word in search_word:
            new_list.append(word)
            break

print(new_list)
