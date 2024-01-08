numbers = list(map(int, input().split(", ")))

even_numbers = []
for index, num in enumerate(numbers):
    if num % 2 == 0:
        even_numbers.append(index)

print(even_numbers)
