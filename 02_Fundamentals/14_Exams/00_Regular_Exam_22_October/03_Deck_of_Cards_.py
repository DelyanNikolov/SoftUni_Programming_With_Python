deck_of_cards = input().split(", ")
commands_count = int(input())

for n in range(commands_count):
    command = input().split(", ")
    if command[0] == "Add":
        card_name = command[1]
        if card_name in deck_of_cards:
            print("Card is already in the deck")
        else:
            deck_of_cards.append(card_name)
            print("Card successfully added")
    elif command[0] == "Remove":
        card_name = command[1]
        if card_name in deck_of_cards:
            deck_of_cards.remove(card_name)
            print("Card successfully removed")
        else:
            print("Card not found")
    elif command[0] == "Remove At":
        card_index = int(command[1])
        if 0 <= card_index < len(deck_of_cards):
            deck_of_cards.pop(card_index)
            print("Card successfully removed")
        else:
            print("Index out of range")
    elif command[0] == "Insert":
        insert_index = int(command[1])
        card_name = command[2]
        if 0 <= insert_index < len(deck_of_cards):
            if card_name not in deck_of_cards:
                deck_of_cards.insert(insert_index, card_name)
                print("Card successfully added")
            else:
                print("Card is already added")
        else:
            print("Index out of range")
print(", ".join(deck_of_cards))
