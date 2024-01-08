basket_price = 1.50
wreath_price = 3.80
chocolate_bunny_price = 7
clients_count = int(input())
sum_of_price = 0
for _ in range(clients_count):
    current_products_count = 0
    total_price = 0
    basket_count = 0
    wreath_count = 0
    chocolate_bunny_count = 0
    discount = 0
    command = input()
    while command != "Finish":
        product = command
        current_products_count += 1
        if product == "basket":
            basket_count += 1
        elif product == "wreath":
            wreath_count += 1
        elif product == "chocolate bunny":
            chocolate_bunny_count += 1
        command = input()
    if current_products_count % 2 == 0:
        discount = 0.2
    total_price = (basket_count * basket_price
                   + wreath_count * wreath_price
                   + chocolate_bunny_count * chocolate_bunny_price) \
                  * (1 - discount)
    sum_of_price += total_price
    print(f"You purchased {current_products_count} items for {total_price :.2f} leva.")
average_price = sum_of_price / clients_count
print(f"Average bill per client is: {average_price :.2f} leva.")
