first_char = input()
last_char = input()
text = input()

first_char_code = ord(first_char)
last_char_code = ord(last_char)
ascii_sum = 0
# ascii_sum = [ord(symbol) for symbol in text if ord(first_char) < ord(symbol) < ord(second_char)]
for letter in text:
    if first_char_code < ord(letter) < last_char_code:
        ascii_sum += ord(letter)
print(ascii_sum)
