numbers = list(input().split())

numbers_inverted = []

for number in numbers:
    current_number = -int(number)
    numbers_inverted.append(current_number)

print(numbers_inverted)
