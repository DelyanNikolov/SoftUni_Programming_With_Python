PENS_PRISE = 5.80
MARKERS_PRISE = 7.20
DETERGENT = 1.2

pens_pcs = int(input())
markers_pcs = int(input())
detergent_liters = int(input())
discount = int(input()) / 100

total_price = pens_pcs * PENS_PRISE + markers_pcs * MARKERS_PRISE + detergent_liters * DETERGENT

total_sum = total_price - total_price * discount

print(total_sum)