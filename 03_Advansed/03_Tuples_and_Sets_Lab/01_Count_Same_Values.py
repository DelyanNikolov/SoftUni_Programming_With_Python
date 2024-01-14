numbers = tuple(float(num) for num in input().split())

num_data = {}

for num in numbers:
    if num not in num_data:
        num_data[num] = numbers.count(num)

for num, count in num_data.items():
    print(f"{num:.1f} - {count} times")
