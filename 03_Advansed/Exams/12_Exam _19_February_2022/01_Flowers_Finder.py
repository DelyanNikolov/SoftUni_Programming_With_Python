from collections import deque

words = ["rose", "tulip", "lotus", "daffodil"]
words_copy = words.copy()
word_found = ""
vowels = deque(input().split(" "))
consonants = input().split(" ")
while True:
    if vowels and consonants:
        vowel = vowels.popleft()
        consonant = consonants.pop()
    else:
        break
    for i in range(len(words)):
        if vowel in words[i]:
            words_copy[i] = words_copy[i].replace(vowel, "")
        if consonant in words[i]:
            words_copy[i] = words_copy[i].replace(consonant, "")
        if not words_copy[i]:
            word_found = words[i]
            break
    if word_found:
        break
if word_found:
    print(f"Word found: {word_found}")
else:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")
