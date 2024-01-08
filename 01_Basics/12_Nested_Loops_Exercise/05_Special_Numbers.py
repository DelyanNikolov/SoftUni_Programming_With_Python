number = int(input())

for num in range(1111, 10000):

    is_special = True
    num_string = str(num)
    for index, digit in enumerate(num_string):
        current_digit = int(digit)
        if current_digit == 0:
            is_special = False
            break
        if number % current_digit != 0:
            is_special = False

    if is_special:
        print(f"{num}", end=" ")
