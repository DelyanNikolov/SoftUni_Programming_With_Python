numbers_count = int(input())
positive_numbers = []
negative_numbers = []
for _ in range(numbers_count):
    current_number = int(input())
    if current_number >= 0:
        positive_numbers.append(current_number)
    elif current_number <0:
        negative_numbers.append(current_number)

print(positive_numbers)
print(negative_numbers)
print(f"Count of positives: {len(positive_numbers)}\nSum of negatives: {sum(negative_numbers)}")

