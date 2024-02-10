def shopping_cart(*products_data):
    limitations = {
        "Soup": 3,
        "Pizza": 4,
        "Dessert": 2
    }
    result = []
    meals_data = {"Soup": [], "Pizza": [], "Dessert": []}
    for item in products_data:
        if item == "Stop":
            break
        meal_type = item[0]
        product = item[1]
        # chek if the max product count is reached
        if limitations[meal_type] <= 0:
            continue
        # if the limit is not reached, adding the product to the corresponding list
        if meal_type not in meals_data:
            meals_data[meal_type] = []
        if product not in meals_data[meal_type]:
            meals_data[meal_type].append(product)
        # reducing the value in limitations
        limitations[meal_type] -= 1
    for meal, products_list in sorted(meals_data.items(), key=lambda x: (-len(x[1]), x[0])):
        result.append(f"{meal}:")
        for prod in sorted(products_list):
            result.append(f" - {prod}")

    if any(meals_data.values()):
        return '\n'.join(result)
    else:
        return "No products in the cart!"


print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))
