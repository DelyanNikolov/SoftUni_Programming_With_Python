def calculate_factorial(some_number):
    factorial = some_number
    for num in range(1, some_number):
        factorial *= num
    return factorial


first_number = int(input())
second_number = int(input())
factorial_first_number = calculate_factorial(first_number)
factorial_second_number = calculate_factorial(second_number)

final_result = factorial_first_number / factorial_second_number

print(f"{final_result:.2f}")
