VIP_TICKET = 499.99
NORMAL_TICKET = 249.99

budget = float(input())
category = input()
people_in_group = int(input())

if people_in_group <= 4:
    transport_cost = 0.75 * budget
elif 5 <= people_in_group <= 9:
    transport_cost = 0.6 * budget
elif 10 <= people_in_group <= 24:
    transport_cost = 0.5 * budget
elif 25 <= people_in_group <= 49:
    transport_cost = 0.4 * budget
elif people_in_group >= 50:
    transport_cost = 0.25 * budget

ticket_cost = 0

if category == "VIP":
    ticket_cost = people_in_group * VIP_TICKET
elif category == "Normal":
    ticket_cost = people_in_group * NORMAL_TICKET

money_left = budget - transport_cost - ticket_cost

if money_left >= 0:
    print(f"Yes! You have {money_left:.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(money_left):.2f} leva.")
