number = int(input())

tribonacci = [1]
list_to_sum = []

for index in range(number - 1):
    list_to_sum = tribonacci[-3:]
    new_num = sum(list_to_sum)
    tribonacci.append(new_num)
for element in tribonacci:
    print(str(element), end=" ")
