# От конзолата се прочитат:
# •	Закупеното количество храна за кученцето в килограми – цяло число в интервала [1 …100]
# •	На всеки следващ ред до получаване на команда Adopted ще получавате колко грама изяжда кученцето на всяко хранене - цяло число в интервала [10 …1000]
food_bought_kg = int(input())
food_bought_gr = food_bought_kg * 1000
total_eaten_food = 0
command = input()
while command != "Adopted":
    current_food = int(command)
    total_eaten_food += current_food
    command = input()

diff = abs(food_bought_gr - total_eaten_food)
if total_eaten_food <= food_bought_gr:
    print(f"Food is enough! Leftovers: {diff} grams.")
else:

    print(f"Food is not enough. You need {diff} grams more.")
