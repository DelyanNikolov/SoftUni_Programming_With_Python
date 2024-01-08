numbers_list = input().split(", ")
numbers_as_int = [int(num) for num in numbers_list]

for index in range(len(numbers_as_int) - 1, -1, -1):
    if int(numbers_as_int[index]) == 0:
        zero = int(numbers_as_int.pop(index))
        numbers_as_int.append(zero)
print(numbers_as_int)
