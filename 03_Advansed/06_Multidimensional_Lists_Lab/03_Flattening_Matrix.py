row_count = int(input())
flatten = []
for i in range(row_count):
    row_data = [int(el) for el in input().split(", ")]
    flatten.extend(row_data)
print(flatten)
