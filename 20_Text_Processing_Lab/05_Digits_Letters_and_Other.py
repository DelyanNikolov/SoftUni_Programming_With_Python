text = input()
digits = ""
letters = ""
symbols = ""

for letter in text:
    if letter.isdigit():
        digits += letter
    elif letter.isalpha():
        letters += letter
    else:
        symbols += letter
print(digits)
print(letters)
print(symbols)
