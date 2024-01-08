numbers_count = int(input())
p1_count = 0
p2_count = 0
p3_count = 0
p4_count = 0
p5_count = 0

for _ in range(numbers_count):
    current_number = int(input())
    if current_number < 200:
        p1_count += 1
    elif current_number < 400:
        p2_count += 1
    elif current_number < 600:
        p3_count += 1
    elif current_number < 800:
        p4_count += 1
    elif current_number >= 800:
        p5_count += 1

p1_percentage = p1_count / numbers_count * 100
p2_percentage = p2_count / numbers_count * 100
p3_percentage = p3_count / numbers_count * 100
p4_percentage = p4_count / numbers_count * 100
p5_percentage = p5_count / numbers_count * 100

print(f"{p1_percentage:.2f}%")
print(f"{p2_percentage:.2f}%")
print(f"{p3_percentage:.2f}%")
print(f"{p4_percentage:.2f}%")
print(f"{p5_percentage:.2f}%")
