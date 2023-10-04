def calculator(operator, num1, num2):
    return {
        'add': num1 + num2,
        'subtract': num1 - num2,
        'divide': int(num1/num2),
        'multiply': num1 * num2
    }.get(operator)


operator = input()
num1 = int(input())
num2 = int(input())

print(calculator(operator, num1, num2))
