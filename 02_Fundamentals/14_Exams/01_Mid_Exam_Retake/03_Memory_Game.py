sequence_of_elements = input().split()
player_choice = input().split()
number_of_moves = 0
while player_choice[0] != "end":
    index_1 = int(player_choice[0])
    index_2 = int(player_choice[1])
    if not sequence_of_elements:
        break
    if index_1 == index_2 or (index_1 < 0 or index_2 < 0) or (index_1 >= len(sequence_of_elements) or index_2 >= len(sequence_of_elements)):
        print("Invalid input! Adding additional elements to the board")
        number_of_moves += 1
        center_of_sequence = (len(sequence_of_elements) + 2) // 2
        sequence_of_elements.insert(center_of_sequence - 1, f"-{number_of_moves}a")
        sequence_of_elements.insert(center_of_sequence, f"-{number_of_moves}a")
    else:
        if sequence_of_elements[index_1] == sequence_of_elements[index_2]:
            print(f"Congrats! You have found matching elements - {sequence_of_elements[index_1]}!")
            number_of_moves += 1
            if index_1 < index_2:
                sequence_of_elements.pop(index_2)
                sequence_of_elements.pop(index_1)
            elif index_1 > index_2:
                sequence_of_elements.pop(index_1)
                sequence_of_elements.pop(index_2)
        else:
            number_of_moves += 1
            print("Try again!")

    player_choice = input().split()
if len(sequence_of_elements) > 0:
    print(f"Sorry you lose :(")
    print(" ".join(map(str, sequence_of_elements)))
else:
    print(f"You have won in {number_of_moves} turns!")
