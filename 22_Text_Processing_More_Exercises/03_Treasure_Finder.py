def find_treasure_type(message):
    treasure = message.split("&")[1]
    return treasure


key_sequence = [int(num) for num in input().split()]

while True:
    text_to_decode = input()
    if text_to_decode == "find":
        break
    decoded_message = ""
    for index_text in range(len(text_to_decode)):
        if index_text < len(key_sequence):
            key_index = index_text
        else:
            key_index = index_text % len(key_sequence)
        decrypted_symbol = chr(ord(text_to_decode[index_text]) - key_sequence[key_index])
        decoded_message += decrypted_symbol

    treasure_type = find_treasure_type(decoded_message)
    treasure_coordinates = decoded_message[decoded_message.index("<") + 1:decoded_message.index(">")]
    print(f"Found {treasure_type} at {treasure_coordinates}")
