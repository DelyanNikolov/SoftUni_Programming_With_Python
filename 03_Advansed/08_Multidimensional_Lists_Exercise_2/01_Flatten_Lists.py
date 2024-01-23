line = input().split("|")
flatten = []
for sub_string in line[::-1]:
    flatten.extend(sub_string.split())

print(*flatten)
