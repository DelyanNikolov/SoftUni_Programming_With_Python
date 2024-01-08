pairs_count = int(input())
sum_of_numbers = 0
current_sum = 0
previous_sum = 0
max_difference = 0
equals = True
for _ in range(pairs_count):
    number_1 = int(input())
    number_2 = int(input())
    current_sum = number_1 + number_2
    if _ != 0 and current_sum != previous_sum:
        equals = False
        current_difference = abs(current_sum - previous_sum)
        if max_difference < current_difference:
            max_difference = current_difference

    previous_sum = current_sum

if equals:
    print(f"Yes, value={previous_sum}")
else:
    print(f"No, maxdiff={max_difference}")
