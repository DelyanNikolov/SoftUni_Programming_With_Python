month = input()
nights_stay = int(input())

studio_discount = 0
ap_discount = 0
studio_price = 0
apartment_price = 0
if month == "May" or month == "October":
    studio_price = 50
    apartment_price = 65
    if 7 < nights_stay <= 14:
        studio_discount = 0.05
    elif nights_stay > 14:
        ap_discount = 0.1
        studio_discount = 0.3
elif month == "June" or month == "September":
    studio_price = 75.20
    apartment_price = 68.70
    if nights_stay > 14:
        studio_discount = 0.2
        ap_discount = 0.1
elif month == "July" or month == "August":
    studio_price = 76
    apartment_price = 77
    if nights_stay > 14:
        ap_discount = 0.1

price_for_stay_studio = (nights_stay * studio_price) * (1 - studio_discount)
price_for_stay_ap = (nights_stay * apartment_price) * (1 - ap_discount)

print(f"Apartment: {price_for_stay_ap:.2f} lv.")
print(f"Studio: {price_for_stay_studio:.2f} lv.")
