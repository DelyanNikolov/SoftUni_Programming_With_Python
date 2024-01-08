numbers_count = int(input())

even_sum = 0
odd_sum = 0

for number in range(1, numbers_count + 1):
    if number % 2 != 0:
        current_number = int(input())
        odd_sum += current_number
    else:
        current_number = int(input())
        even_sum += current_number


if odd_sum == even_sum:
    print("Yes")
    print(f"Sum = {even_sum}")
else:
    difference = abs(even_sum - odd_sum)
    print("No")
    print(f"Diff = {difference}")
