detergent_bottles_count = int(input())
detergent_in_ml = detergent_bottles_count * 750
pots_cycle = 0
dishes_count = 0
pots_count = 0

while True:
    command = input()
    if command == "End":
        break
    current_dishes_count = int(command)
    pots_cycle += 1

    if pots_cycle % 3 == 0:
        detergent_in_ml -= current_dishes_count * 15
        pots_count += current_dishes_count
    else:
        detergent_in_ml -= current_dishes_count * 5
        dishes_count += current_dishes_count

    if detergent_in_ml <= 0:
        break

if command == "End":
    print("Detergent was enough!")
    print(f"{dishes_count} dishes and {pots_count} pots were washed.")
    print(f"Leftover detergent {detergent_in_ml} ml.")
else:
    print(f"Not enough detergent, {-detergent_in_ml} ml. more necessary!")
