def sorting_cheeses(**kwargs):
    result = ""
    sorted_result = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
    for item, quantity in sorted_result:
        result += f"{item}\n"
        for q in sorted(quantity, reverse=True):
            result += f"{q}\n"
    return result


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
