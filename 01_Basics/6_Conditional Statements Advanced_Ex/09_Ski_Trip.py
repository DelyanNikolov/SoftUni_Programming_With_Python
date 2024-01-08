
days_stay = int(input())
type_of_stay = input()      #"room for one person", "apartment" или "president apartment"
feedback = input()          #"positive"  или "negative"

room_for_оne = 18.00
apartment = 25.00
president_apartment = 35.00

nights = days_stay - 1
discount_room_for_one = 0
discount_apartment = 0
discount_president_apartment = 0
cost = 0

if days_stay < 10:
    discount_apartment = 0.3
    discount_president_apartment = 0.1
elif 10 <= days_stay <= 15:
    discount_apartment = 0.35
    discount_president_apartment = 0.15
elif days_stay > 15:
    discount_apartment = 0.50
    discount_president_apartment = 0.20

if type_of_stay == "room for one person":
    cost = nights * room_for_оne
elif type_of_stay == "apartment":
    cost = nights * apartment * (1 - discount_apartment)
elif type_of_stay == "president apartment":
    cost = nights * president_apartment * (1 - discount_president_apartment)

if feedback == "positive":
    total_cost = cost * 1.25
elif feedback == "negative":
    total_cost = cost * 0.9

print(f"{total_cost:.2f}")
