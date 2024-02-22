def cookbook(*data):
    result = []
    recipes = {}

    for item in data:
        recipe_name = item[0]
        cuisine = item[1]
        products = item[2]
        if cuisine not in recipes:
            recipes[cuisine] = {recipe_name: products}
        recipes[cuisine][recipe_name] = products
    for cuisine_nationality, recipe_info in sorted(recipes.items(), key=lambda x: (-len(x[1]), x[0])):
        result.append(f"{cuisine_nationality} cuisine contains {len(recipe_info)} recipes:")
        for recipe_name, recipe_products in sorted(recipe_info.items(), key=lambda kvp: (kvp[0])):
            result.append(f"  * {recipe_name} -> Ingredients: {', '.join(recipe_products)}")

    return '\n'.join(result)


print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"]),
    ("Sushi Rolls", "Japanese", ["rice", "nori", "fish", "vegetables"]),
    ("Miso Soup", "Japanese", ["tofu", "seaweed", "green onions"]),
    ("Guacamole", "Mexican", ["avocado", "tomato", "onion", "lime"])
    ))
