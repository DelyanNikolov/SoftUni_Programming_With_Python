def shopping_list(money, **products_info):
    result = []
    budget = money
    products_bought = 0
    if money >= 100:
        for product_name, data in products_info.items():
            if products_bought >= 5:
                break
            price = data[0]
            quantity = data[1]
            total_cost_of_product = price * quantity
            if total_cost_of_product <= budget:
                products_bought += 1
                result.append(f"You bought {product_name} for {total_cost_of_product:.2f} leva.")
                budget -= total_cost_of_product
    else:
        result.append("You do not have enough budget.")

    return '\n'.join(result)


print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
