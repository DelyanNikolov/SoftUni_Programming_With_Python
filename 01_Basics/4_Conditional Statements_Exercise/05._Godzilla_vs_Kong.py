# •	Декорът за филма е на стойност 10% от бюджета.
# •	При повече от 150 статиста,  има отстъпка за облеклото на стойност 10%.


# •	Ако  парите за декора и дрехите са повече от бюджета:
# o	"Not enough money!"
# o	"Wingard needs {парите недостигащи за филма} leva more."
# •	Ако парите за декора и дрехите са по малко или равни на бюджета:
# o	"Action!"
# o	"Wingard starts filming with {останалите пари} leva left."
# Резултатът трябва да е форматиран до втория знак след десетичната запетая.
film_budget = float(input())
extra_count = int(input())
price_for_costume_per_extra = float(input())
decor = film_budget * 0.1
discount = 0
if extra_count > 150:
    discount = 0.1

money_for_decor_and_costumes = decor + extra_count * (price_for_costume_per_extra * (1 - discount))
lack_money_message = f"Not enough money! \nWingard needs {money_for_decor_and_costumes - film_budget:.2f} leva more."
enough_money_message = f"Action! \nWingard starts filming with {film_budget - money_for_decor_and_costumes:.2f} leva left."

if money_for_decor_and_costumes > film_budget:
    print(lack_money_message)
else:
    print(enough_money_message)
