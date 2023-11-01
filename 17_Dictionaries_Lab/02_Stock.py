line = input().split()
products = {}

for i in range(0, len(line), 2):
    key = line[i]
    value = line[i+1]
    products[key] = value

search_products = input().split()
for product in search_products:
    if product in products:
        print(f"We have {products[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
