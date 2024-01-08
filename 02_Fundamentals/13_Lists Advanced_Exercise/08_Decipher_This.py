secret_message = input().split()
decoded_message = []

for word in secret_message:
    numbers = []
    letters = []
    for symbol in word:
        if symbol.isdigit():
            numbers.append(symbol)
        else:
            letters.append(symbol)

    letter = chr(int("".join(numbers)))
    letters[0], letters[-1] = letters[-1], letters[0]
    switched_word = "".join(letters)
    decoded_word = letter + switched_word
    decoded_message.append(decoded_word)

print(" ".join(decoded_message))
