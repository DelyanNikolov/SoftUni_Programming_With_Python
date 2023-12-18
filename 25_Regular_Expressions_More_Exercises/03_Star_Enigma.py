import re

msg_count = int(input())

for msg in range(msg_count):
    message = input()
    regex = r"[STARstar]"
    pattern = r"@([A-Z][a-z]+)[^\@\-\!\:\>]*:(\d+)[^\@\-\!\:\>]*\!([AD])\![^\@\-\!\:\>]*\->(\d+)"
    result = re.findall(regex, message)
    code = len(result)
    decrypted = [chr(ord(letter)-code) for letter in message]
    print("".join(decrypted))
