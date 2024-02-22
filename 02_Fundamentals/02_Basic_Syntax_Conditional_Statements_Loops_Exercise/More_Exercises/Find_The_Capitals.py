word = input()
upper_letters_index_list = []
for index in range(0, len(word)):
    if word[index].isupper():
        upper_letters_index_list.append(index)
print(upper_letters_index_list)
