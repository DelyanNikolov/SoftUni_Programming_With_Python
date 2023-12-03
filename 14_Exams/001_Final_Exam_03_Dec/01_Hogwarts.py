valid_spells = ["Abracadabra", "Abjuration", "Necromancy", "Illusion", "Divination", "Alteration"]

spell_to_decrypt = input()

while True:
    command = input().split(" ")
    if not command[0] in valid_spells:
        print("The spell did not work!")
    elif command[0] == "Abracadabra":
        break
    elif command[0] == "Abjuration":
        spell_to_decrypt = spell_to_decrypt.upper()
        print(spell_to_decrypt)
    elif command[0] == "Necromancy":
        spell_to_decrypt = spell_to_decrypt.lower()
        print(spell_to_decrypt)
    elif command[0] == "Illusion":
        index = int(command[1])
        letter = command[2]
        if index in range(len(spell_to_decrypt)):
            spell_to_decrypt = spell_to_decrypt[:index] + letter + spell_to_decrypt[index + 1:]
            print("Done!")
        else:
            print("The spell was too weak.")
    elif command[0] == "Divination":
        first_substring = command[1]
        second_substring = command[2]
        spell_to_decrypt = spell_to_decrypt.replace(first_substring, second_substring)
        print(spell_to_decrypt)
    elif command[0] == "Alteration":
        string_to_replace = command[1]
        spell_to_decrypt = spell_to_decrypt.replace(string_to_replace, "")
        print(spell_to_decrypt)
