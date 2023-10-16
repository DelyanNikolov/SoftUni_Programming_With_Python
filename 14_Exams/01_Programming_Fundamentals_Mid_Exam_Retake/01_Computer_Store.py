discount = 1
taxes = 0.2
total_price_without_taxes = 0

while True:
    command = input()
    if command == "regular":
        break
    elif command == "special":
        discount = 0.9
        break
    current_price = float(command)
    if current_price < 0:
        print("Invalid price!")
        continue
    else:
        total_price_without_taxes += current_price

total_amount_of_taxes = total_price_without_taxes * taxes
total_price_with_taxes = (total_price_without_taxes + total_amount_of_taxes) * discount
if total_price_without_taxes <= 0:
    print("Invalid order!")
else:
    print(f"Congratulations you've just bought a new computer!\n"
          f"Price without taxes: {total_price_without_taxes:.2f}$\n"
          f"Taxes: {total_amount_of_taxes:.2f}$\n"
          f"-----------\n"
          f"Total price: {total_price_with_taxes:.2f}$")
