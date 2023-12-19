import re

msg_count = int(input())
final_result = {"Attacked planets": [], "Destroyed planets": []}
for msg in range(msg_count):
    message = input()
    regex = r"(?i)[star]"
    pattern = r"@([A-Z][a-z]+)[^\@\-\!\:\>]*:(\d+)[^\@\-\!\:\>]*\!([AD])\![^\@\-\!\:\>]*\->(\d+)"
    result = re.findall(regex, message)
    code = len(result)
    decrypted_list = [chr(ord(letter) - code) for letter in message]
    decrypted_message = "".join(decrypted_list)
    planets = re.findall(pattern, decrypted_message)
    for item in planets:
        if item[2] == "A":
            final_result["Attacked planets"].append(item[0])
        elif item[2] == "D":
            final_result["Destroyed planets"].append(item[0])

for planet in final_result:
    print(f"{planet}: {len(final_result[planet])}")
    for info in sorted(final_result[planet]):
        print(f"-> {info}")
