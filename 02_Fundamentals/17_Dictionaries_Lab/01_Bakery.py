line = input().split()
products = {}

for i in range(0, len(line), 2):
    key = line[i]
    value = int(line[i + 1])
    products[key] = value
print(products)
