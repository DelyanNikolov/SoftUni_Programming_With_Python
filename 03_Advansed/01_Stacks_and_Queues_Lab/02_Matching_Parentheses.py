expression = input()
indexes = []
for index in range(len(expression)):
    if expression[index] == "(":
        indexes.append(index)
    elif expression[index] == ")":
        start_i = indexes.pop()
        end_i = index + 1
        print(expression[start_i:end_i])
