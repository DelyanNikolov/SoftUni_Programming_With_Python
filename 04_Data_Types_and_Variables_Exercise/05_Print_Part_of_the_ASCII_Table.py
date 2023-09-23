start_index = int(input())
end_index = int(input())

for index in range(start_index, end_index + 1):
    character = chr(index)
    print(character, end=" ")
