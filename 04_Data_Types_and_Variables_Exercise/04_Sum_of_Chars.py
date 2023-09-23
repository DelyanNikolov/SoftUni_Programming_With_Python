numbers_count = int(input())
sum_of_ascii = 0
for _ in range(numbers_count):
    current_number = input()
    code = ord(current_number)
    sum_of_ascii += code

print(f"The sum equals: {sum_of_ascii}")
