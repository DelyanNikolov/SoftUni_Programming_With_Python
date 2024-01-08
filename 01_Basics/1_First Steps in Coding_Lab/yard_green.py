print("Въведи площ в кв.м")
sqwarem = float(input())
price = sqwarem * 7.61
dicount = price * 0.18
endprice = price - dicount
print(f"Крайната цена е: {endprice} лв.")
print(f"Отстъпката е: {dicount} лв.")
