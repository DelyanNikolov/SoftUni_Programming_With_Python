first_char = input()
second_char = input()
text = input()

first_char_code = ord(first_char)
second_char_code = ord(second_char)
ascii_sum = 0
for letter in text:
    if first_char_code < ord(letter) < second_char_code:
        ascii_sum += ord(letter)
print(ascii_sum)
