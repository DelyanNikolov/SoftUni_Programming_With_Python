starting_number = int(input())
final_number = int(input())
magic_number = int(input())
combination_found = False
combinations_counter = 0

for first_number in range(starting_number, final_number + 1):
    for second_number in range(starting_number, final_number + 1):
        combinations_counter += 1
        if first_number + second_number == magic_number:
            combination_found = True
            break
    if combination_found == True:
        break
if combination_found:
    print(f"Combination N:{combinations_counter} ({first_number} + {second_number} = {magic_number})")
else:
    print(f"{combinations_counter} combinations - neither equals {magic_number}")
