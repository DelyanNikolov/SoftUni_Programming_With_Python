message = input()
code = 3
encrypted_msg = ""
for char in message:
    crypt_char = chr(ord(char) + code)
    encrypted_msg += crypt_char

print(encrypted_msg)
