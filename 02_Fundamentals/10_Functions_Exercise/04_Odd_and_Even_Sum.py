def sum_of_even_odd_digits(num):
    odd_sum = 0
    even_sum = 0
    for digit in num:
        if int(digit) % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)
    return odd_sum, even_sum


number = input()

sum_of_odd_digits, sum_of_even_digits = sum_of_even_odd_digits(number)
print(f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}")
