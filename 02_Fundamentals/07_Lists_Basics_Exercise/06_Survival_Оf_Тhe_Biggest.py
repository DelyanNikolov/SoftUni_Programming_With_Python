numbers = input().split()
remove_count = int(input())
list_of_numbers = []
for number in numbers:
    list_of_numbers.append(int(number))

for index in range(remove_count):
    min_number = min(list_of_numbers)
    list_of_numbers.remove(min_number)
list_of_numbers_string = ""
for index in range(len(list_of_numbers)):
    list_of_numbers_string += str(list_of_numbers[index]) + ", "
list_of_numbers_string = list_of_numbers_string[:-2]

print(list_of_numbers_string)
