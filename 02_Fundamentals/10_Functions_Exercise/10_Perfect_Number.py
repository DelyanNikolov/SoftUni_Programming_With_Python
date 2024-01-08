def is_number_perfect(num):
    sum_of_divisors = 0
    for divisor in range(1, num):
        if num % divisor == 0:
            sum_of_divisors += divisor
    if sum_of_divisors == num:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


number = int(input())
print(is_number_perfect(number))
