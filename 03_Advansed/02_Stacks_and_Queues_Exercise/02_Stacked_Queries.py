queries_count = int(input())

numbers_stack = []

for q in range(queries_count):
    query = input().split()
    if query[0] == "1":
        number = int(query[1])
        numbers_stack.append(number)
    elif query[0] == "2":
        if numbers_stack:
            numbers_stack.pop()
    elif query[0] == "3":
        if numbers_stack:
            print(max(numbers_stack))
    elif query[0] == "4":
        if numbers_stack:
            print(min(numbers_stack))

numbers_stack.reverse()
print(*numbers_stack, sep=", ")
