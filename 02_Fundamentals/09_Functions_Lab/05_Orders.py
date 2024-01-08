def snacks(choice, count):
    return {
        'coffee': 1.50 * count,
        'water': 1.00 * count,
        'coke': 1.40 * count,
        'snacks': 2.00 * count
    }.get(choice)


user_choice = input()
quantity = int(input())

print(f"{snacks(user_choice, quantity):.2f}")
