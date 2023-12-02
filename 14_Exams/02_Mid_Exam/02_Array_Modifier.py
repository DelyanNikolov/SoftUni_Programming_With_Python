array_of_integers = [int(num) for num in input().split()]
command = input().split()

while not command[0] == "end":
    if command[0] == "swap":
        index_1 = int(command[1])
        index_2 = int(command[2])
        array_of_integers[index_1], array_of_integers[index_2] = array_of_integers[index_2], array_of_integers[index_1]
    elif command[0] == "multiply":
        index_1 = int(command[1])
        index_2 = int(command[2])
        product = array_of_integers[index_1] * array_of_integers[index_2]
        array_of_integers[index_1] = product
    elif command[0] == "decrease":
        array_of_integers = [num - 1 for num in array_of_integers]
    command = input().split()
print(", ".join(map(str, array_of_integers)))
