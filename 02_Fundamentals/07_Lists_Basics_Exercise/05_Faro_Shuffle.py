deck_of_cards = input().split()
shuffles_count = int(input())

for _ in range(shuffles_count):
    shuffled_deck = []
    middle_of_deck = len(deck_of_cards) // 2

    left_part = deck_of_cards[0:middle_of_deck]
    right_part = deck_of_cards[middle_of_deck:]

    for index in range(len(left_part)):
        shuffled_deck.append(left_part[index])
        shuffled_deck.append(right_part[index])
    deck_of_cards = shuffled_deck

print(shuffled_deck)
