
junior_cyclists = int(input())
senior_cyclists = int(input())
trail_type = input()

junior_tax = 0
senior_tax = 0
tax_discount = 0
expense = 0.95  # 5% expenses for organising event

if trail_type == "trail":
    junior_tax = 5.50
    senior_tax = 7
elif trail_type == "cross-country":
    junior_tax = 8
    senior_tax = 9.50
    if (junior_cyclists + senior_cyclists) >= 50:
        tax_discount = 0.25
elif trail_type == "downhill":
    junior_tax = 12.25
    senior_tax = 13.75
elif trail_type == "road":
    junior_tax = 20.00
    senior_tax = 21.50

total_funds = (junior_cyclists * junior_tax + senior_cyclists * senior_tax) * (1 - tax_discount) * expense

print(f"{total_funds:.2f}")
