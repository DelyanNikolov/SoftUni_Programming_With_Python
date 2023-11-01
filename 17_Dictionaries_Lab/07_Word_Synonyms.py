count_of_words = int(input())
synonyms = {}
for _ in range(count_of_words):
    word = input()
    synonym = input()
    if word not in synonyms:
        synonyms[word] = [synonym]
    else:
        synonyms[word].append(synonym)

for word in synonyms:
    print(f"{word} - {', '.join(synonyms[word])}")
