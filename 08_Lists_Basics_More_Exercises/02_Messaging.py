numbers = input().split()
string = input()
string_as_list = list(string)
message = ""

for letter in range(len(numbers)):
    num_set = numbers[letter]
    index = 0
    for i in range(len(num_set)):
        index += int(num_set[i])
    if index > (len(string_as_list) - 1):
        index = index - (len(string_as_list) - 1) - 1
    letter = string_as_list.pop(index)
    message += letter

print(message)
