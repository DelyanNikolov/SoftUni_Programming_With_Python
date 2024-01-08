factor = int(input())
count = int(input())
multiplied_numbers = []

for number in range(1, count + 1):
    multiplied_number = number * factor
    multiplied_numbers.append(multiplied_number)

print(multiplied_numbers)
