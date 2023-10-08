numbers_list = input().split(" ")
numbers_list = map(int, numbers_list)

even_numbers = list(filter(lambda x: x % 2 == 0, numbers_list))

print(even_numbers)
