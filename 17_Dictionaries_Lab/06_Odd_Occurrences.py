words = input().split()
occurrences = {}
for word in words:
    word_lower = word.lower()
    if word_lower not in occurrences:
        occurrences[word_lower] = 1
    else:
        occurrences[word_lower] += 1

for key, value in occurrences.items():
    if value % 2 != 0:
        print(key, end=" ")
