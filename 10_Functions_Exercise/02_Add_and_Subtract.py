def sum_numbers(num1, num2):
    answer = num1 + num2
    return answer


def subtract(result, num3):
    return result - num3


def add_and_subtract(num1, num2, num3):
    print(subtract(sum_numbers(num1, num2), num3))


first_num = int(input())
second_num = int(input())
third_num = int(input())

add_and_subtract(first_num, second_num, third_num)
