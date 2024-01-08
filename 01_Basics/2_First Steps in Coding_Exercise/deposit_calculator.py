#сума = депозирана сума  + срок на депозита * ((депозирана сума * годишен лихвен процент ) / 12)
deposit_amount = float(input())
deposit_months = int(input())
annual_interest_rate = float(input()) / 100

final_amounth = deposit_amount + deposit_months * ((deposit_amount * annual_interest_rate)/12)

print(final_amounth)