number = int(input())
number_as_str = str(number)
max_number = ""
digits = []
for item in number_as_str:
    digits.append(int(item))
digits.sort(reverse=True)
for digit in digits:
    max_number += str(digit)
print(max_number)
