numbers = list(map(int, input().split(", ")))
positive = [num for num in numbers if num >= 0]
negative = [num for num in numbers if num < 0]
even = [num for num in numbers if num % 2 == 0]
odd = [num for num in numbers if num % 2 != 0]
print("Positive:", ", ".join(list(map(str, positive))))
print("Negative:", ", ".join(list(map(str, negative))))
print("Even:", ", ".join(list(map(str, even))))
print("Odd:", ", ".join(list(map(str, odd))))
