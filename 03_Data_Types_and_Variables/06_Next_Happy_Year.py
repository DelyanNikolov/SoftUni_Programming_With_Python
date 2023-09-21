current_year = int(input())
next_happy_year = 0
while True:
    current_year += 1
    digits = str(current_year)
    for digit in digits:
        same_digit_count = digits.count(digit)
        if same_digit_count > 1:
            break
    else:
        next_happy_year = digits
        print(next_happy_year)
        break
