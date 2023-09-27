parts_list = []
for _ in range(3):
    data = input()
    parts_list.append(data)

parts_list[0], parts_list[2] = parts_list[2], parts_list[0]

print(parts_list)