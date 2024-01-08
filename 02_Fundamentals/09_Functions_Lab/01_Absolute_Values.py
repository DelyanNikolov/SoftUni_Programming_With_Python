def abs_value(data):
    absolute_values = []
    num_list = data
    for num in num_list:
        absolute = abs(float(num))
        absolute_values.append(absolute)
    return absolute_values


numbers = input().split()
print(abs_value(numbers))
