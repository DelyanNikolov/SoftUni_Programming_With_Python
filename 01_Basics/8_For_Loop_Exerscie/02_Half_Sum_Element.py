import sys

max_number = -sys.maxsize
sum_of_numbers = 0

numbers_count = int(input())

for num in range(numbers_count):
    current_number = int(input())
    if current_number > max_number:
        max_number = current_number
    sum_of_numbers += current_number

rest_of_sum = sum_of_numbers - max_number

if max_number == rest_of_sum:
    print(f"Yes\nSum = {max_number}")
else:
    diff = abs(max_number - rest_of_sum)
    print(f"No\nDiff = {diff}")
