encrypted_message = input()

while True:
    command = input().split("|")
    if command[0] == "Decode":
        break
    elif command[0] == "Move":  # Moves the first n letters to the back of the string
        number_of_letters = int(command[1])
        encrypted_message = encrypted_message[number_of_letters:] + encrypted_message[:number_of_letters]
    elif command[0] == "Insert":  # Inserts the given value before the given index in the string
        index = int(command[1])
        value = command[2]
        encrypted_message = encrypted_message[:index] + value + encrypted_message[index:]
    elif command[0] == "ChangeAll": # Changes all occurrences of the given substring with the replacement text
        substring = command[1]
        replacement_string = command[2]
        encrypted_message = encrypted_message.replace(substring, replacement_string)
print(f"The decrypted message is: {encrypted_message}")
