import re


def calculate_cool_threshold(some_string):
    threshold = 1
    for char in some_string:
        if char.isdigit():
            threshold *= int(char)
    return threshold


def calculate_emoji_coolness(emoji):
    coolness = 0
    for letter in emoji:
        coolness += ord(letter)
    return coolness


sentence = input()
regex = r"::[A-Z][a-z]{2,}\b::|\*\*[A-Z][a-z]{2,}\b\*\*"
matches = re.findall(regex, sentence)
cool_threshold = calculate_cool_threshold(sentence)
words_in_text = [word for word in sentence.split()]
only_cool_emojis = []
for match in matches:
    word = match[2:-2]
    emoji_coolness = calculate_emoji_coolness(word)
    if emoji_coolness >= cool_threshold:
        only_cool_emojis.append(match)

print(f"Cool threshold: {cool_threshold}")
print(f"{len(matches)} emojis found in the text. The cool ones are:")
print(" \n".join(only_cool_emojis))
