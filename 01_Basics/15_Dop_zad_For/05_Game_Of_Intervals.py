moves_count = int(input())
score = 0
from_0_to_9 = 0
from_10_to_19 = 0
from_20_to_29 = 0
from_30_to_39 = 0
from_40_to_50 = 0
invalid_numbers = 0

for _ in range(moves_count):
    current_number = int(input())
    if 0 <= current_number <= 9:
        from_0_to_9 += 1
        score += current_number * 0.2
    elif 10 <= current_number <= 19:
        from_10_to_19 += 1
        score += current_number * 0.3
    elif 20 <= current_number <= 29:
        from_20_to_29 += 1
        score += current_number * 0.4
    elif 30 <= current_number <= 39:
        from_30_to_39 += 1
        score += 50
    elif 40 <= current_number <= 50:
        from_40_to_50 += 1
        score += 100
    elif current_number < 0 or current_number > 50:
        invalid_numbers += 1
        score /= 2

from_0_to_9_percentage = from_0_to_9 / moves_count * 100
from_10_to_19_percentage = from_10_to_19 / moves_count * 100
from_20_to_29_percentage = from_20_to_29 / moves_count * 100
from_30_to_39_percentage = from_30_to_39 / moves_count * 100
from_40_to_50_percentage = from_40_to_50 / moves_count * 100
invalid_numbers_percentage = invalid_numbers / moves_count * 100

print(f"{score:.2f}")
print(f"From 0 to 9: {from_0_to_9_percentage:.2f}%")
print(f"From 10 to 19: {from_10_to_19_percentage:.2f}%")
print(f"From 20 to 29: {from_20_to_29_percentage:.2f}%")
print(f"From 30 to 39: {from_30_to_39_percentage:.2f}%")
print(f"From 40 to 50: {from_40_to_50_percentage:.2f}%")
print(f"Invalid numbers: {invalid_numbers_percentage:.2f}%")
