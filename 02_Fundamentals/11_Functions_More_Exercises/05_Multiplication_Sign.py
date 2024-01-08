def finds_multiplication(n1, n2, n3):
    negative_count = 0
    list_of_nums = [n1, n2, n3]
    for num in list_of_nums:
        if num < 0:
            negative_count += 1

    if 0 in list_of_nums:
        return "zero"
    elif negative_count % 2 == 0:
        return "positive"
    elif negative_count % 2 != 0:
        return "negative"


num1 = int(input())
num2 = int(input())
num3 = int(input())
print(finds_multiplication(num1, num2, num3))
