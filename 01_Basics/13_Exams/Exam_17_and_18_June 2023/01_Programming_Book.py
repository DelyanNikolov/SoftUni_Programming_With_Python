# Входът от конзолата съдържа 5 реда:
# •	Цена за отпечатване на една страница - реално число в интервала (0.00…1.50]
# •	Цена за отпечатване на една корица - реално число в интервала (0.00…5.00]
# •	Процентно намаление за отпечатване на хартия - цяло число в интервала (0…100]
# •	Сумата, която трябва да се заплати на дизайнер - реално число в интервала (0.00…150.00]
# •	Процент от цялата дължима сума, който е заплатен от екипа - цяло число в интервала [0…100]
cost_of_page = float(input())
cost_of_cover = float(input())
discount_percent = int(input())
designer_cost = float(input())
money_from_team_percent = int(input())

cost_of_print = cost_of_page * 899 + cost_of_cover * 2
cost_of_print_with_discount = (cost_of_print * (1 - discount_percent / 100)) + designer_cost
total_cost = cost_of_print_with_discount * (1 - money_from_team_percent / 100)
print(f"Avtonom should pay {total_cost :.2f} BGN.")
