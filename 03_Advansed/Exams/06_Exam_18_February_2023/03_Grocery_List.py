def shop_from_grocery_list(budget, grocery_list, *products):
    result = []
    for product_name, product_price in products:
        if product_name in grocery_list and budget >= product_price:
            grocery_list.remove(product_name)
            budget -= product_price

        if budget < product_price:
            break
    if not grocery_list:
        result.append(f"Shopping is successful. Remaining budget: {budget:.2f}.")
    else:
        result.append(f"You did not buy all the products. Missing products: {', '.join(grocery_list)}.")

    return "\n".join(result)


print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))
